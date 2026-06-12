"""Generated from Smithy shape ``com.amazonaws.securityhub#InvitationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.invitation

InvitationList: TypeAlias = list["aws_sdk_securityhub.types.invitation.Invitation"]


# --- restJson1 ser/de ---
def serialize_json(value: InvitationList) -> list:
    import aws_sdk_securityhub.types.invitation

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.invitation.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvitationList:
    import aws_sdk_securityhub.types.invitation

    out: InvitationList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.invitation.deserialize_json(item))
    return out
