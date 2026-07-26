"""Generated from Smithy shape ``com.amazonaws.connect#Applications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.application

Applications: TypeAlias = list["capo_connect.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: Applications) -> list:
    import capo_connect.types.application

    out: list = []
    for item in value:
        out.append(capo_connect.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> Applications:
    import capo_connect.types.application

    out: Applications = []
    for item in data:
        out.append(capo_connect.types.application.deserialize_json(item))
    return out
