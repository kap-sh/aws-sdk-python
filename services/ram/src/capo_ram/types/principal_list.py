"""Generated from Smithy shape ``com.amazonaws.ram#PrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.principal

PrincipalList: TypeAlias = list["capo_ram.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalList) -> list:
    import capo_ram.types.principal

    out: list = []
    for item in value:
        out.append(capo_ram.types.principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrincipalList:
    import capo_ram.types.principal

    out: PrincipalList = []
    for item in data:
        out.append(capo_ram.types.principal.deserialize_json(item))
    return out
