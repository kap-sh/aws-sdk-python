"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfEndpointType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.endpoint_type

ListOfEndpointType: TypeAlias = list[
    "aws_sdk_api_gateway.types.endpoint_type.EndpointType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfEndpointType) -> list:
    import aws_sdk_api_gateway.types.endpoint_type

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.endpoint_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfEndpointType:
    import aws_sdk_api_gateway.types.endpoint_type

    out: ListOfEndpointType = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.endpoint_type.deserialize_json(item))
    return out
