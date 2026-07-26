"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.group_status
    import capo_qbusiness.types.timestamp


class GroupStatusDetail(TypedDict, closed=True):
    status: NotRequired["capo_qbusiness.types.group_status.GroupStatus"]
    """<p>The status of a group.</p>"""
    last_updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated.</p>"""
    error_detail: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>The details of an error associated a group status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupStatusDetail) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_qbusiness.types.group_status

        out["status"] = capo_qbusiness.types.group_status.serialize_json(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["lastUpdatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "error_detail" in value:
        import capo_qbusiness.types.error_detail

        out["errorDetail"] = capo_qbusiness.types.error_detail.serialize_json(
            value["error_detail"]
        )
    return out


def deserialize_json(data: dict) -> GroupStatusDetail:
    out: GroupStatusDetail = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_qbusiness.types.group_status

        out["status"] = capo_qbusiness.types.group_status.deserialize_json(
            data["status"]
        )
    if "lastUpdatedAt" in data:
        import capo_qbusiness.types.timestamp

        out["last_updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "errorDetail" in data:
        import capo_qbusiness.types.error_detail

        out["error_detail"] = capo_qbusiness.types.error_detail.deserialize_json(
            data["errorDetail"]
        )
    return out
