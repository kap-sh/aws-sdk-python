"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MLSyntheticDataParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.column_classification_details
    import aws_sdk_cleanrooms.types.max_membership_inference_attack_score


class MLSyntheticDataParameters(TypedDict):
    epsilon: "float"
    """<p>The epsilon value for differential privacy when generating synthetic data. Lower values provide stronger privacy guarantees but may reduce data utility.</p>"""
    max_membership_inference_attack_score: "aws_sdk_cleanrooms.types.max_membership_inference_attack_score.MaxMembershipInferenceAttackScore"
    """<p>The maximum acceptable score for membership inference attack vulnerability. Synthetic data generation fails if the score for the resulting data exceeds this threshold.</p>"""
    column_classification: "aws_sdk_cleanrooms.types.column_classification_details.ColumnClassificationDetails"
    """<p>Classification details for data columns that specify how each column should be treated during synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLSyntheticDataParameters) -> dict:
    out: dict = {}
    out["epsilon"] = value["epsilon"]
    out["maxMembershipInferenceAttackScore"] = value[
        "max_membership_inference_attack_score"
    ]
    import aws_sdk_cleanrooms.types.column_classification_details

    out["columnClassification"] = (
        aws_sdk_cleanrooms.types.column_classification_details.serialize_json(
            value["column_classification"]
        )
    )
    return out


def deserialize_json(data: dict) -> MLSyntheticDataParameters:
    out: MLSyntheticDataParameters = {}  # type: ignore[typeddict-item]
    if "epsilon" in data:
        out["epsilon"] = data["epsilon"]
    else:
        raise DeserializationError("MLSyntheticDataParameters.epsilon required")
    if "maxMembershipInferenceAttackScore" in data:
        out["max_membership_inference_attack_score"] = data[
            "maxMembershipInferenceAttackScore"
        ]
    else:
        raise DeserializationError(
            "MLSyntheticDataParameters.max_membership_inference_attack_score required"
        )
    if "columnClassification" in data:
        import aws_sdk_cleanrooms.types.column_classification_details

        out["column_classification"] = (
            aws_sdk_cleanrooms.types.column_classification_details.deserialize_json(
                data["columnClassification"]
            )
        )
    else:
        raise DeserializationError(
            "MLSyntheticDataParameters.column_classification required"
        )
    return out
