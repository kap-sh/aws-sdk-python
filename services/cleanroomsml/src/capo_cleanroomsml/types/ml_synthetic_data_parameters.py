"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MLSyntheticDataParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.column_classification_details


class MLSyntheticDataParameters(TypedDict, closed=True):
    epsilon: "float"
    """<p>The epsilon value for differential privacy, which controls the privacy-utility tradeoff in synthetic data generation. Lower values provide stronger privacy guarantees but may reduce data utility.</p>"""
    max_membership_inference_attack_score: "float"
    """<p>The maximum acceptable score for membership inference attack vulnerability. Synthetic data generation fails if the score for the resulting data exceeds this threshold.</p>"""
    column_classification: NotRequired[
        "capo_cleanroomsml.types.column_classification_details.ColumnClassificationDetails"
    ]
    """<p>Classification details for data columns that specify how each column should be treated during synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLSyntheticDataParameters) -> dict:
    out: dict = {}
    out["epsilon"] = value["epsilon"]
    out["maxMembershipInferenceAttackScore"] = value[
        "max_membership_inference_attack_score"
    ]
    if "column_classification" in value:
        import capo_cleanroomsml.types.column_classification_details

        out["columnClassification"] = (
            capo_cleanroomsml.types.column_classification_details.serialize_json(
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
        import capo_cleanroomsml.types.column_classification_details

        out["column_classification"] = (
            capo_cleanroomsml.types.column_classification_details.deserialize_json(
                data["columnClassification"]
            )
        )
    return out
