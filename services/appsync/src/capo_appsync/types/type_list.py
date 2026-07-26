"""Generated from Smithy shape ``com.amazonaws.appsync#TypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.type

TypeList: TypeAlias = list["capo_appsync.types.type.Type"]


# --- restJson1 ser/de ---
def serialize_json(value: TypeList) -> list:
    import capo_appsync.types.type

    out: list = []
    for item in value:
        out.append(capo_appsync.types.type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TypeList:
    import capo_appsync.types.type

    out: TypeList = []
    for item in data:
        out.append(capo_appsync.types.type.deserialize_json(item))
    return out
