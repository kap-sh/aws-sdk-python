"""Generated from Smithy shape ``com.amazonaws.ram#PrincipalArnOrIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.string

PrincipalArnOrIdList: TypeAlias = list["aws_sdk_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalArnOrIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrincipalArnOrIdList:
    return list(data)
