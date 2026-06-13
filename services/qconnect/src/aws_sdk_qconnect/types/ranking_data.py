"""Generated from Smithy shape ``com.amazonaws.qconnect#RankingData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.relevance_level
    import aws_sdk_qconnect.types.relevance_score


class RankingData(TypedDict):
    relevance_score: "aws_sdk_qconnect.types.relevance_score.RelevanceScore"
    """<p>The relevance level of the recommendation.</p>"""
    relevance_level: NotRequired[
        "aws_sdk_qconnect.types.relevance_level.RelevanceLevel"
    ]
    """<p>The relevance score of the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RankingData) -> dict:
    out: dict = {}
    out["relevanceScore"] = value.get("relevance_score", 0)
    if "relevance_level" in value:
        out["relevanceLevel"] = value["relevance_level"]
    return out


def deserialize_json(data: dict) -> RankingData:
    out: RankingData = {}  # type: ignore[typeddict-item]
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    else:
        out["relevance_score"] = 0
    if "relevanceLevel" in data:
        out["relevance_level"] = data["relevanceLevel"]
    return out
