"""Generated from Smithy shape ``com.amazonaws.appsync#ApiKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_key

ApiKeys: TypeAlias = list["aws_sdk_appsync.types.api_key.ApiKey"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeys) -> list:
    import aws_sdk_appsync.types.api_key

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.api_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApiKeys:
    import aws_sdk_appsync.types.api_key

    out: ApiKeys = []
    for item in data:
        out.append(aws_sdk_appsync.types.api_key.deserialize_json(item))
    return out
