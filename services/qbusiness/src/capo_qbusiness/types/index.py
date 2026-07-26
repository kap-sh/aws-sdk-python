"""Generated from Smithy shape ``com.amazonaws.qbusiness#Index``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.index_name
    import capo_qbusiness.types.index_status
    import capo_qbusiness.types.timestamp


class Index(TypedDict, closed=True):
    display_name: NotRequired["capo_qbusiness.types.index_name.IndexName"]
    """<p>The name of the index.</p>"""
    index_id: NotRequired["capo_qbusiness.types.index_id.IndexId"]
    """<p>The identifier for the index.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the index was created.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the index was last updated.</p>"""
    status: NotRequired["capo_qbusiness.types.index_status.IndexStatus"]
    """<p>The current status of the index. When the status is <code>ACTIVE</code>, the index is ready.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Index) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "status" in value:
        import capo_qbusiness.types.index_status

        out["status"] = capo_qbusiness.types.index_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> Index:
    out: Index = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    if "createdAt" in data:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "status" in data:
        import capo_qbusiness.types.index_status

        out["status"] = capo_qbusiness.types.index_status.deserialize_json(
            data["status"]
        )
    return out
