"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfUsage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_long

ListOfUsage: TypeAlias = list["aws_sdk_api_gateway.types.list_of_long.ListOfLong"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUsage) -> list:
    import aws_sdk_api_gateway.types.list_of_long

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.list_of_long.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfUsage:
    import aws_sdk_api_gateway.types.list_of_long

    out: ListOfUsage = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.list_of_long.deserialize_json(item))
    return out
