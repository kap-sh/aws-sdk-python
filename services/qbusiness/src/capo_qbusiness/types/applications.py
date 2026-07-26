"""Generated from Smithy shape ``com.amazonaws.qbusiness#Applications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.application

Applications: TypeAlias = list["capo_qbusiness.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: Applications) -> list:
    import capo_qbusiness.types.application

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> Applications:
    import capo_qbusiness.types.application

    out: Applications = []
    for item in data:
        out.append(capo_qbusiness.types.application.deserialize_json(item))
    return out
