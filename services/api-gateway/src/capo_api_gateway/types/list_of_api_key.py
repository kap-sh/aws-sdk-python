"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfApiKey``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.api_key

ListOfApiKey: TypeAlias = list["capo_api_gateway.types.api_key.ApiKey"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfApiKey) -> list:
    import capo_api_gateway.types.api_key

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.api_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfApiKey:
    import capo_api_gateway.types.api_key

    out: ListOfApiKey = []
    for item in data:
        out.append(capo_api_gateway.types.api_key.deserialize_json(item))
    return out
