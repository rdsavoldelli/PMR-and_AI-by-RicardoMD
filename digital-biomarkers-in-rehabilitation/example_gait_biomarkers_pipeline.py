"""
Example: Conceptual gait digital biomarkers pipeline

Author: Ricardo Diaz Savoldelli, MD
Focus: Bridge between clinical gait analysis and AI thinking in rehabilitation

This script is NOT intended for clinical decision-making.
It is a didactic example of how gait-related digital biomarkers
could be processed and used in a simple ML workflow.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def simulate_gait_data(n_samples=200, random_state=42):
    """
    Simulate a simple dataset representing gait-related digital biomarkers.
    For a real application, this would come from inertial sensors, pressure insoles, etc.
    """
    rng = np.random.RandomState(random_state)

    # Features (conceptual):
    # - gait_speed (m/s)
    # - step_time_variability (s)
    # - step_length_asymmetry (%)
    # - stance_phase_ratio (% of gait cycle)
    gait_speed = rng.normal(loc=1.0, scale=0.2, size=n_samples)             # slower = higher risk
    step_time_variability = rng.normal(loc=0.05, scale=0.02, size=n_samples)  # higher = less stable
    step_length_asymmetry = rng.normal(loc=5.0, scale=3.0, size=n_samples) # higher = less symmetry
    stance_phase_ratio = rng.normal(loc=60.0, scale=5.0, size=n_samples)   # % of gait cycle

    # Simple rule-based label (for illustration):
    # "1" = high fall risk, "0" = low fall risk
    risk_score = (
        (gait_speed < 0.8).astype(int)
        + (step_time_variability > 0.07).astype(int)
        + (step_length_asymmetry > 8).astype(int)
    )
    labels = (risk_score >= 2).astype(int)

    data = pd.DataFrame({
        "gait_speed": gait_speed,
        "step_time_variability": step_time_variability,
        "step_length_asymmetry": step_length_asymmetry,
        "stance_phase_ratio": stance_phase_ratio,
        "high_fall_risk": labels,
    })

    return data


def run_simple_model():
    """
    Run a basic ML pipeline to classify high vs low fall risk
    based on simulated gait digital biomarkers.
    """
    data = simulate_gait_data()

    X = data[["gait_speed",
              "step_time_variability",
              "step_length_asymmetry",
              "stance_phase_ratio"]]
    y = data["high_fall_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("=== Classification report: High vs Low fall risk ===")
    print(classification_report(y_test, y_pred))

    feature_importances = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    print("\n=== Feature importance (clinical intuition check) ===")
    print(feature_importances)


if __name__ == "__main__":
    run_simple_model()
