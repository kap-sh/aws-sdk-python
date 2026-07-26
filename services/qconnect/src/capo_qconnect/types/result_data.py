"""Generated from Smithy shape ``com.amazonaws.qconnect#ResultData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary
    import capo_qconnect.types.document
    import capo_qconnect.types.query_result_type
    import capo_qconnect.types.relevance_score
    import capo_qconnect.types.uuid


class ResultData(TypedDict, closed=True):
    result_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the result data.</p>"""
    document: NotRequired["capo_qconnect.types.document.Document"]
    """<p>The document.</p>"""
    relevance_score: "capo_qconnect.types.relevance_score.RelevanceScore"
    """<p>The relevance score of the results.</p>"""
    data: NotRequired["capo_qconnect.types.data_summary.DataSummary"]
    """<p> Summary of the recommended content.</p>"""
    type: NotRequired["capo_qconnect.types.query_result_type.QueryResultType"]
    """<p>The type of the query result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultData) -> dict:
    out: dict = {}
    out["resultId"] = value["result_id"]
    if "document" in value:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.serialize_json(value["document"])
    out["relevanceScore"] = value.get("relevance_score", 0)
    if "data" in value:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.serialize_json(value["data"])
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ResultData:
    out: ResultData = {}  # type: ignore[typeddict-item]
    if "resultId" in data:
        out["result_id"] = data["resultId"]
    else:
        raise DeserializationError("ResultData.result_id required")
    if "document" in data:
        import capo_qconnect.types.document

        out["document"] = capo_qconnect.types.document.deserialize_json(
            data["document"]
        )
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    else:
        out["relevance_score"] = 0
    if "data" in data:
        import capo_qconnect.types.data_summary

        out["data"] = capo_qconnect.types.data_summary.deserialize_json(data["data"])
    if "type" in data:
        out["type"] = data["type"]
    return out
