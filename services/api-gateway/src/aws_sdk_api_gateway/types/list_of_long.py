"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfLong``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.long

ListOfLong: TypeAlias = list["aws_sdk_api_gateway.types.long.Long"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLong) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfLong:
    return list(data)
