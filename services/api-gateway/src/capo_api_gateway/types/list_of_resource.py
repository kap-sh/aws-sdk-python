"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.resource

ListOfResource: TypeAlias = list["capo_api_gateway.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfResource) -> list:
    import capo_api_gateway.types.resource

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfResource:
    import capo_api_gateway.types.resource

    out: ListOfResource = []
    for item in data:
        out.append(capo_api_gateway.types.resource.deserialize_json(item))
    return out
