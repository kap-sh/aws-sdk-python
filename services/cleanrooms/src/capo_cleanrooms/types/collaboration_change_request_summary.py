"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationChangeRequestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.approval_statuses
    import capo_cleanrooms.types.change_list
    import capo_cleanrooms.types.change_request_status
    import capo_cleanrooms.types.uuid


class CollaborationChangeRequestSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier for the change request.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier for the collaboration.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the change request was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time when the change request was last updated.</p>"""
    status: "capo_cleanrooms.types.change_request_status.ChangeRequestStatus"
    """<p>The current status of the change request.</p>"""
    is_auto_approved: "bool"
    """<p>Whether the change request was automatically approved.</p>"""
    changes: "capo_cleanrooms.types.change_list.ChangeList"
    """<p>Summary of the changes in this change request.</p>"""
    approvals: NotRequired["capo_cleanrooms.types.approval_statuses.ApprovalStatuses"]
    """<p>Summary of approval statuses from all collaboration members for this change request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationChangeRequestSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["collaborationId"] = value["collaboration_id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.change_request_status

    out["status"] = capo_cleanrooms.types.change_request_status.serialize_json(
        value["status"]
    )
    out["isAutoApproved"] = value["is_auto_approved"]
    import capo_cleanrooms.types.change_list

    out["changes"] = capo_cleanrooms.types.change_list.serialize_json(value["changes"])
    if "approvals" in value:
        import capo_cleanrooms.types.approval_statuses

        out["approvals"] = capo_cleanrooms.types.approval_statuses.serialize_json(
            value["approvals"]
        )
    return out


def deserialize_json(data: dict) -> CollaborationChangeRequestSummary:
    out: CollaborationChangeRequestSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationChangeRequestSummary.id required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationChangeRequestSummary.collaboration_id required"
        )
    if "createTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError(
            "CollaborationChangeRequestSummary.create_time required"
        )
    if "updateTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError(
            "CollaborationChangeRequestSummary.update_time required"
        )
    if "status" in data:
        import capo_cleanrooms.types.change_request_status

        out["status"] = capo_cleanrooms.types.change_request_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CollaborationChangeRequestSummary.status required")
    if "isAutoApproved" in data:
        out["is_auto_approved"] = data["isAutoApproved"]
    else:
        raise DeserializationError(
            "CollaborationChangeRequestSummary.is_auto_approved required"
        )
    if "changes" in data:
        import capo_cleanrooms.types.change_list

        out["changes"] = capo_cleanrooms.types.change_list.deserialize_json(
            data["changes"]
        )
    else:
        raise DeserializationError("CollaborationChangeRequestSummary.changes required")
    if "approvals" in data:
        import capo_cleanrooms.types.approval_statuses

        out["approvals"] = capo_cleanrooms.types.approval_statuses.deserialize_json(
            data["approvals"]
        )
    return out
