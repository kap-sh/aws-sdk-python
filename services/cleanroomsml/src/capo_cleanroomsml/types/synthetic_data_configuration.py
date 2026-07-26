"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#SyntheticDataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.ml_synthetic_data_parameters
    import capo_cleanroomsml.types.synthetic_data_evaluation_scores


class SyntheticDataConfiguration(TypedDict, closed=True):
    synthetic_data_parameters: (
        "capo_cleanroomsml.types.ml_synthetic_data_parameters.MLSyntheticDataParameters"
    )
    """<p>The parameters that control how synthetic data is generated, including privacy settings, column classifications, and other configuration options that affect the data synthesis process.</p>"""
    synthetic_data_evaluation_scores: NotRequired[
        "capo_cleanroomsml.types.synthetic_data_evaluation_scores.SyntheticDataEvaluationScores"
    ]
    """<p>Evaluation scores that assess the quality and privacy characteristics of the generated synthetic data, providing metrics on data utility and privacy preservation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataConfiguration) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.ml_synthetic_data_parameters

    out["syntheticDataParameters"] = (
        capo_cleanroomsml.types.ml_synthetic_data_parameters.serialize_json(
            value["synthetic_data_parameters"]
        )
    )
    if "synthetic_data_evaluation_scores" in value:
        import capo_cleanroomsml.types.synthetic_data_evaluation_scores

        out["syntheticDataEvaluationScores"] = (
            capo_cleanroomsml.types.synthetic_data_evaluation_scores.serialize_json(
                value["synthetic_data_evaluation_scores"]
            )
        )
    return out


def deserialize_json(data: dict) -> SyntheticDataConfiguration:
    out: SyntheticDataConfiguration = {}  # type: ignore[typeddict-item]
    if "syntheticDataParameters" in data:
        import capo_cleanroomsml.types.ml_synthetic_data_parameters

        out["synthetic_data_parameters"] = (
            capo_cleanroomsml.types.ml_synthetic_data_parameters.deserialize_json(
                data["syntheticDataParameters"]
            )
        )
    else:
        raise DeserializationError(
            "SyntheticDataConfiguration.synthetic_data_parameters required"
        )
    if "syntheticDataEvaluationScores" in data:
        import capo_cleanroomsml.types.synthetic_data_evaluation_scores

        out["synthetic_data_evaluation_scores"] = (
            capo_cleanroomsml.types.synthetic_data_evaluation_scores.deserialize_json(
                data["syntheticDataEvaluationScores"]
            )
        )
    return out
