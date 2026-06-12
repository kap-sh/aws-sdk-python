"""Generated from Smithy shape ``com.amazonaws.ram#PrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.principal

PrincipalList: TypeAlias = list["aws_sdk_ram.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalList) -> list:
    import aws_sdk_ram.types.principal

    out: list = []
    for item in value:
        out.append(aws_sdk_ram.types.principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrincipalList:
    import aws_sdk_ram.types.principal

    out: PrincipalList = []
    for item in data:
        out.append(aws_sdk_ram.types.principal.deserialize_json(item))
    return out
