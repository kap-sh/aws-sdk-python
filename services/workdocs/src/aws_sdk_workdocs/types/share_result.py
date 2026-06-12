"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.message_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.role_type
    import aws_sdk_workdocs.types.share_status_type


class ShareResult(TypedDict):
    principal_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the principal.</p>"""
    invitee_principal_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the invited user.</p>"""
    role: NotRequired["aws_sdk_workdocs.types.role_type.RoleType"]
    """<p>The role.</p>"""
    status: NotRequired["aws_sdk_workdocs.types.share_status_type.ShareStatusType"]
    """<p>The status.</p>"""
    share_id: NotRequired["aws_sdk_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the resource that was shared.</p>"""
    status_message: NotRequired["aws_sdk_workdocs.types.message_type.MessageType"]
    """<p>The status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareResult) -> dict:
    out: dict = {}
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "invitee_principal_id" in value:
        out["InviteePrincipalId"] = value["invitee_principal_id"]
    if "role" in value:
        import aws_sdk_workdocs.types.role_type

        out["Role"] = aws_sdk_workdocs.types.role_type.serialize_json(value["role"])
    if "status" in value:
        import aws_sdk_workdocs.types.share_status_type

        out["Status"] = aws_sdk_workdocs.types.share_status_type.serialize_json(
            value["status"]
        )
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ShareResult:
    out: ShareResult = {}  # type: ignore[typeddict-item]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "InviteePrincipalId" in data:
        out["invitee_principal_id"] = data["InviteePrincipalId"]
    if "Role" in data:
        import aws_sdk_workdocs.types.role_type

        out["role"] = aws_sdk_workdocs.types.role_type.deserialize_json(data["Role"])
    if "Status" in data:
        import aws_sdk_workdocs.types.share_status_type

        out["status"] = aws_sdk_workdocs.types.share_status_type.deserialize_json(
            data["Status"]
        )
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
