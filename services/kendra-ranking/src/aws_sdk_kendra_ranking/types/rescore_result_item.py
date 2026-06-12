"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreResultItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.document_id
    import aws_sdk_kendra_ranking.types.float


class RescoreResultItem(TypedDict):
    document_id: NotRequired["aws_sdk_kendra_ranking.types.document_id.DocumentId"]
    """<p>The identifier of the document from the search service.</p>"""
    score: NotRequired["aws_sdk_kendra_ranking.types.float.Float"]
    """<p>The relevancy score or rank that Amazon Kendra Intelligent Ranking gives to the result.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreResultItem) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreResultItem:
    out: RescoreResultItem = {}  # type: ignore[typeddict-item]
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "Score" in data:
        out["score"] = data["Score"]
    return out
