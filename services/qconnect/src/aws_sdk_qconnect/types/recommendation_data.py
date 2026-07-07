"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.data_summary
    import aws_sdk_qconnect.types.document
    import aws_sdk_qconnect.types.recommendation_id
    import aws_sdk_qconnect.types.recommendation_type
    import aws_sdk_qconnect.types.relevance_level
    import aws_sdk_qconnect.types.relevance_score


class RecommendationData(TypedDict, closed=True):
    recommendation_id: "aws_sdk_qconnect.types.recommendation_id.RecommendationId"
    """<p>The identifier of the recommendation.</p>"""
    document: NotRequired["aws_sdk_qconnect.types.document.Document"]
    """<p>The recommended document.</p>"""
    relevance_score: "aws_sdk_qconnect.types.relevance_score.RelevanceScore"
    """<p>The relevance score of the recommendation.</p>"""
    relevance_level: NotRequired[
        "aws_sdk_qconnect.types.relevance_level.RelevanceLevel"
    ]
    """<p>The relevance level of the recommendation.</p>"""
    type: NotRequired["aws_sdk_qconnect.types.recommendation_type.RecommendationType"]
    """<p>The type of recommendation.</p>"""
    data: NotRequired["aws_sdk_qconnect.types.data_summary.DataSummary"]
    """<p> Summary of the recommended content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationData) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    if "document" in value:
        import aws_sdk_qconnect.types.document

        out["document"] = aws_sdk_qconnect.types.document.serialize_json(
            value["document"]
        )
    out["relevanceScore"] = value.get("relevance_score", 0)
    if "relevance_level" in value:
        out["relevanceLevel"] = value["relevance_level"]
    if "type" in value:
        out["type"] = value["type"]
    if "data" in value:
        import aws_sdk_qconnect.types.data_summary

        out["data"] = aws_sdk_qconnect.types.data_summary.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> RecommendationData:
    out: RecommendationData = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError("RecommendationData.recommendation_id required")
    if "document" in data:
        import aws_sdk_qconnect.types.document

        out["document"] = aws_sdk_qconnect.types.document.deserialize_json(
            data["document"]
        )
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    else:
        out["relevance_score"] = 0
    if "relevanceLevel" in data:
        out["relevance_level"] = data["relevanceLevel"]
    if "type" in data:
        out["type"] = data["type"]
    if "data" in data:
        import aws_sdk_qconnect.types.data_summary

        out["data"] = aws_sdk_qconnect.types.data_summary.deserialize_json(data["data"])
    return out
