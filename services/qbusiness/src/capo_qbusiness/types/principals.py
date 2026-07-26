"""Generated from Smithy shape ``com.amazonaws.qbusiness#Principals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.principal

Principals: TypeAlias = list["capo_qbusiness.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: Principals) -> list:
    import capo_qbusiness.types.principal

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> Principals:
    import capo_qbusiness.types.principal

    out: Principals = []
    for item in data:
        out.append(capo_qbusiness.types.principal.deserialize_json(item))
    return out
