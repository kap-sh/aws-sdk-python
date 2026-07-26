"""Generated from Smithy shape ``com.amazonaws.qbusiness#ScoreAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.score_confidence


class ScoreAttributes(TypedDict, closed=True):
    score_confidence: NotRequired[
        "capo_qbusiness.types.score_confidence.ScoreConfidence"
    ]
    """<p>The confidence level of the relevance score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScoreAttributes) -> dict:
    out: dict = {}
    if "score_confidence" in value:
        import capo_qbusiness.types.score_confidence

        out["scoreConfidence"] = capo_qbusiness.types.score_confidence.serialize_json(
            value["score_confidence"]
        )
    return out


def deserialize_json(data: dict) -> ScoreAttributes:
    out: ScoreAttributes = {}  # type: ignore[typeddict-item]
    if "scoreConfidence" in data:
        import capo_qbusiness.types.score_confidence

        out["score_confidence"] = (
            capo_qbusiness.types.score_confidence.deserialize_json(
                data["scoreConfidence"]
            )
        )
    return out
