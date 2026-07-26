"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadShareSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.permission_type
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.share_status
    import capo_wellarchitected.types.shared_with
    import capo_wellarchitected.types.status_message


class WorkloadShareSummary(TypedDict, closed=True):
    share_id: NotRequired["capo_wellarchitected.types.share_id.ShareId"]
    shared_with: NotRequired["capo_wellarchitected.types.shared_with.SharedWith"]
    permission_type: NotRequired[
        "capo_wellarchitected.types.permission_type.PermissionType"
    ]
    status: NotRequired["capo_wellarchitected.types.share_status.ShareStatus"]
    status_message: NotRequired[
        "capo_wellarchitected.types.status_message.StatusMessage"
    ]
    """<p>Optional message to compliment the Status field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadShareSummary) -> dict:
    out: dict = {}
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "permission_type" in value:
        import capo_wellarchitected.types.permission_type

        out["PermissionType"] = (
            capo_wellarchitected.types.permission_type.serialize_json(
                value["permission_type"]
            )
        )
    if "status" in value:
        import capo_wellarchitected.types.share_status

        out["Status"] = capo_wellarchitected.types.share_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> WorkloadShareSummary:
    out: WorkloadShareSummary = {}  # type: ignore[typeddict-item]
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    if "SharedWith" in data:
        out["shared_with"] = data["SharedWith"]
    if "PermissionType" in data:
        import capo_wellarchitected.types.permission_type

        out["permission_type"] = (
            capo_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    if "Status" in data:
        import capo_wellarchitected.types.share_status

        out["status"] = capo_wellarchitected.types.share_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
