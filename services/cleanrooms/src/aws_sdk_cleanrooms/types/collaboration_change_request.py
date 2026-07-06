"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.approval_statuses
    import aws_sdk_cleanrooms.types.change_list
    import aws_sdk_cleanrooms.types.change_request_status
    import aws_sdk_cleanrooms.types.uuid


class CollaborationChangeRequest(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier for the change request.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier for the collaboration being modified.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the change request was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time when the change request was last updated.</p>"""
    status: "aws_sdk_cleanrooms.types.change_request_status.ChangeRequestStatus"
    """<p>The current status of the change request. Valid values are <code>PENDING</code>, <code>APPROVED</code>, <code>DENIED</code>, <code>COMMITTED</code>, and <code>CANCELLED</code>.</p>"""
    is_auto_approved: "bool"
    """<p>Whether the change request was automatically approved based on the collaboration's auto-approval settings.</p>"""
    changes: "aws_sdk_cleanrooms.types.change_list.ChangeList"
    """<p>The list of changes specified in this change request.</p>"""
    approvals: NotRequired[
        "aws_sdk_cleanrooms.types.approval_statuses.ApprovalStatuses"
    ]
    """<p>A list of approval details from collaboration members, including approval status and multi-party approval workflow information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationChangeRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["collaborationId"] = value["collaboration_id"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.change_request_status

    out["status"] = aws_sdk_cleanrooms.types.change_request_status.serialize_json(
        value["status"]
    )
    out["isAutoApproved"] = value["is_auto_approved"]
    import aws_sdk_cleanrooms.types.change_list

    out["changes"] = aws_sdk_cleanrooms.types.change_list.serialize_json(
        value["changes"]
    )
    if "approvals" in value:
        import aws_sdk_cleanrooms.types.approval_statuses

        out["approvals"] = aws_sdk_cleanrooms.types.approval_statuses.serialize_json(
            value["approvals"]
        )
    return out


def deserialize_json(data: dict) -> CollaborationChangeRequest:
    out: CollaborationChangeRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationChangeRequest.id required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationChangeRequest.collaboration_id required"
        )
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("CollaborationChangeRequest.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("CollaborationChangeRequest.update_time required")
    if "status" in data:
        import aws_sdk_cleanrooms.types.change_request_status

        out["status"] = aws_sdk_cleanrooms.types.change_request_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CollaborationChangeRequest.status required")
    if "isAutoApproved" in data:
        out["is_auto_approved"] = data["isAutoApproved"]
    else:
        raise DeserializationError(
            "CollaborationChangeRequest.is_auto_approved required"
        )
    if "changes" in data:
        import aws_sdk_cleanrooms.types.change_list

        out["changes"] = aws_sdk_cleanrooms.types.change_list.deserialize_json(
            data["changes"]
        )
    else:
        raise DeserializationError("CollaborationChangeRequest.changes required")
    if "approvals" in data:
        import aws_sdk_cleanrooms.types.approval_statuses

        out["approvals"] = aws_sdk_cleanrooms.types.approval_statuses.deserialize_json(
            data["approvals"]
        )
    return out
