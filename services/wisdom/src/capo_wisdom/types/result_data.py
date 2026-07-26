"""Generated from Smithy shape ``com.amazonaws.wisdom#ResultData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.document
    import capo_wisdom.types.relevance_score
    import capo_wisdom.types.uuid


class ResultData(TypedDict, closed=True):
    result_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the result data.</p>"""
    document: "capo_wisdom.types.document.Document"
    """<p>The document.</p>"""
    relevance_score: "capo_wisdom.types.relevance_score.RelevanceScore"
    """<p>The relevance score of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultData) -> dict:
    out: dict = {}
    out["resultId"] = value["result_id"]
    import capo_wisdom.types.document

    out["document"] = capo_wisdom.types.document.serialize_json(value["document"])
    out["relevanceScore"] = value.get("relevance_score", 0)
    return out


def deserialize_json(data: dict) -> ResultData:
    out: ResultData = {}  # type: ignore[typeddict-item]
    if "resultId" in data:
        out["result_id"] = data["resultId"]
    else:
        raise DeserializationError("ResultData.result_id required")
    if "document" in data:
        import capo_wisdom.types.document

        out["document"] = capo_wisdom.types.document.deserialize_json(data["document"])
    else:
        raise DeserializationError("ResultData.document required")
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    else:
        out["relevance_score"] = 0
    return out
