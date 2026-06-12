"""Generated from Smithy shape ``com.amazonaws.appsync#Apis``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api

Apis: TypeAlias = list["aws_sdk_appsync.types.api.Api"]


# --- restJson1 ser/de ---
def serialize_json(value: Apis) -> list:
    import aws_sdk_appsync.types.api

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.api.serialize_json(item))
    return out


def deserialize_json(data: list) -> Apis:
    import aws_sdk_appsync.types.api

    out: Apis = []
    for item in data:
        out.append(aws_sdk_appsync.types.api.deserialize_json(item))
    return out
