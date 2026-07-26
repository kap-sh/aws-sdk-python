"""Generated from Smithy shape ``com.amazonaws.qbusiness#AccessControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.access_control

AccessControls: TypeAlias = list["capo_qbusiness.types.access_control.AccessControl"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControls) -> list:
    import capo_qbusiness.types.access_control

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.access_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessControls:
    import capo_qbusiness.types.access_control

    out: AccessControls = []
    for item in data:
        out.append(capo_qbusiness.types.access_control.deserialize_json(item))
    return out
