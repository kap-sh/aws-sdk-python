"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CrlDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.crl_detail

CrlDetails: TypeAlias = list["capo_rolesanywhere.types.crl_detail.CrlDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: CrlDetails) -> list:
    import capo_rolesanywhere.types.crl_detail

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.crl_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrlDetails:
    import capo_rolesanywhere.types.crl_detail

    out: CrlDetails = []
    for item in data:
        out.append(capo_rolesanywhere.types.crl_detail.deserialize_json(item))
    return out
