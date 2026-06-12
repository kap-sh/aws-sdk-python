"""Generated from Smithy shape ``com.amazonaws.kendra#ScoreAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.score_confidence


class ScoreAttributes(TypedDict):
    score_confidence: NotRequired[
        "aws_sdk_kendra.types.score_confidence.ScoreConfidence"
    ]
    """<p>A relative ranking for how relevant the response is to the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScoreAttributes) -> dict:
    out: dict = {}
    if "score_confidence" in value:
        import aws_sdk_kendra.types.score_confidence

        out["ScoreConfidence"] = (
            aws_sdk_kendra.types.score_confidence.serialize_aws_json_1_1(
                value["score_confidence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScoreAttributes:
    out: ScoreAttributes = {}  # type: ignore[typeddict-item]
    if "ScoreConfidence" in data:
        import aws_sdk_kendra.types.score_confidence

        out["score_confidence"] = (
            aws_sdk_kendra.types.score_confidence.deserialize_aws_json_1_1(
                data["ScoreConfidence"]
            )
        )
    return out
