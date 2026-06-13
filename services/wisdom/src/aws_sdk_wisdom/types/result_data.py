"""Generated from Smithy shape ``com.amazonaws.wisdom#ResultData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.document
    import aws_sdk_wisdom.types.relevance_score
    import aws_sdk_wisdom.types.uuid


class ResultData(TypedDict):
    result_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the result data.</p>"""
    document: "aws_sdk_wisdom.types.document.Document"
    """<p>The document.</p>"""
    relevance_score: "aws_sdk_wisdom.types.relevance_score.RelevanceScore"
    """<p>The relevance score of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultData) -> dict:
    out: dict = {}
    out["resultId"] = value["result_id"]
    import aws_sdk_wisdom.types.document

    out["document"] = aws_sdk_wisdom.types.document.serialize_json(value["document"])
    out["relevanceScore"] = value.get("relevance_score", 0)
    return out


def deserialize_json(data: dict) -> ResultData:
    out: ResultData = {}  # type: ignore[typeddict-item]
    if "resultId" in data:
        out["result_id"] = data["resultId"]
    else:
        raise DeserializationError("ResultData.result_id required")
    if "document" in data:
        import aws_sdk_wisdom.types.document

        out["document"] = aws_sdk_wisdom.types.document.deserialize_json(
            data["document"]
        )
    else:
        raise DeserializationError("ResultData.document required")
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    else:
        out["relevance_score"] = 0
    return out
