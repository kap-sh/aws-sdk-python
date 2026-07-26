"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.application

ApplicationsList: TypeAlias = list["capo_mgn.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationsList) -> list:
    import capo_mgn.types.application

    out: list = []
    for item in value:
        out.append(capo_mgn.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationsList:
    import capo_mgn.types.application

    out: ApplicationsList = []
    for item in data:
        out.append(capo_mgn.types.application.deserialize_json(item))
    return out
