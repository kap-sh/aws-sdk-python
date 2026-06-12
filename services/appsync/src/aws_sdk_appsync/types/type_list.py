"""Generated from Smithy shape ``com.amazonaws.appsync#TypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.type

TypeList: TypeAlias = list["aws_sdk_appsync.types.type.Type"]


# --- restJson1 ser/de ---
def serialize_json(value: TypeList) -> list:
    import aws_sdk_appsync.types.type

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TypeList:
    import aws_sdk_appsync.types.type

    out: TypeList = []
    for item in data:
        out.append(aws_sdk_appsync.types.type.deserialize_json(item))
    return out
