"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfEndpointType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.endpoint_type

ListOfEndpointType: TypeAlias = list[
    "capo_api_gateway.types.endpoint_type.EndpointType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfEndpointType) -> list:
    import capo_api_gateway.types.endpoint_type

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.endpoint_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfEndpointType:
    import capo_api_gateway.types.endpoint_type

    out: ListOfEndpointType = []
    for item in data:
        out.append(capo_api_gateway.types.endpoint_type.deserialize_json(item))
    return out
