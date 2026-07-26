"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfRestApi``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.rest_api

ListOfRestApi: TypeAlias = list["capo_api_gateway.types.rest_api.RestApi"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRestApi) -> list:
    import capo_api_gateway.types.rest_api

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.rest_api.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfRestApi:
    import capo_api_gateway.types.rest_api

    out: ListOfRestApi = []
    for item in data:
        out.append(capo_api_gateway.types.rest_api.deserialize_json(item))
    return out
