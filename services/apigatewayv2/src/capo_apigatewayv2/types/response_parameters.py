"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ResponseParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.integration_parameters

ResponseParameters: TypeAlias = dict[
    "capo_apigatewayv2.types.__string.__string",
    "capo_apigatewayv2.types.integration_parameters.IntegrationParameters",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResponseParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_apigatewayv2.types.integration_parameters

        out[key] = capo_apigatewayv2.types.integration_parameters.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ResponseParameters:
    out: ResponseParameters = {}
    for key, value in data.items():
        import capo_apigatewayv2.types.integration_parameters

        out[key] = capo_apigatewayv2.types.integration_parameters.deserialize_json(
            value
        )
    return out
