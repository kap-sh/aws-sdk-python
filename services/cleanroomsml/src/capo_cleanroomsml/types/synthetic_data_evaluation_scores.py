"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#SyntheticDataEvaluationScores``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.data_privacy_scores


class SyntheticDataEvaluationScores(TypedDict, closed=True):
    data_privacy_scores: "capo_cleanroomsml.types.data_privacy_scores.DataPrivacyScores"
    """<p>Privacy-specific evaluation scores that measure how well the synthetic data protects individual privacy, including assessments of potential privacy risks such as membership inference attacks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataEvaluationScores) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.data_privacy_scores

    out["dataPrivacyScores"] = (
        capo_cleanroomsml.types.data_privacy_scores.serialize_json(
            value["data_privacy_scores"]
        )
    )
    return out


def deserialize_json(data: dict) -> SyntheticDataEvaluationScores:
    out: SyntheticDataEvaluationScores = {}  # type: ignore[typeddict-item]
    if "dataPrivacyScores" in data:
        import capo_cleanroomsml.types.data_privacy_scores

        out["data_privacy_scores"] = (
            capo_cleanroomsml.types.data_privacy_scores.deserialize_json(
                data["dataPrivacyScores"]
            )
        )
    else:
        raise DeserializationError(
            "SyntheticDataEvaluationScores.data_privacy_scores required"
        )
    return out
