"""Generated from Smithy shape ``com.amazonaws.kendra#ScoreAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.score_confidence


class ScoreAttributes(TypedDict, closed=True):
    score_confidence: NotRequired["capo_kendra.types.score_confidence.ScoreConfidence"]
    """<p>A relative ranking for how relevant the response is to the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScoreAttributes) -> dict:
    out: dict = {}
    if "score_confidence" in value:
        import capo_kendra.types.score_confidence

        out["ScoreConfidence"] = (
            capo_kendra.types.score_confidence.serialize_aws_json_1_1(
                value["score_confidence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScoreAttributes:
    out: ScoreAttributes = {}  # type: ignore[typeddict-item]
    if "ScoreConfidence" in data:
        import capo_kendra.types.score_confidence

        out["score_confidence"] = (
            capo_kendra.types.score_confidence.deserialize_aws_json_1_1(
                data["ScoreConfidence"]
            )
        )
    return out
