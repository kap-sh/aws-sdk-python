"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.resource

ListOfResource: TypeAlias = list["aws_sdk_api_gateway.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfResource) -> list:
    import aws_sdk_api_gateway.types.resource

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfResource:
    import aws_sdk_api_gateway.types.resource

    out: ListOfResource = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.resource.deserialize_json(item))
    return out
