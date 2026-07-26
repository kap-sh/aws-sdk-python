"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfIntegrationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.integration_response
    import capo_api_gateway.types.string

MapOfIntegrationResponse: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.integration_response.IntegrationResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfIntegrationResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.integration_response

        out[key] = capo_api_gateway.types.integration_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfIntegrationResponse:
    out: MapOfIntegrationResponse = {}
    for key, value in data.items():
        import capo_api_gateway.types.integration_response

        out[key] = capo_api_gateway.types.integration_response.deserialize_json(value)
    return out
