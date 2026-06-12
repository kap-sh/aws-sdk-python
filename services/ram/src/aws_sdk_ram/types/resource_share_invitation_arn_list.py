"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.string

ResourceShareInvitationArnList: TypeAlias = list["aws_sdk_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceShareInvitationArnList:
    return list(data)
