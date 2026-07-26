"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RouteSettingsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.route_settings

RouteSettingsMap: TypeAlias = dict[
    "capo_apigatewayv2.types.__string.__string",
    "capo_apigatewayv2.types.route_settings.RouteSettings",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RouteSettingsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_apigatewayv2.types.route_settings

        out[key] = capo_apigatewayv2.types.route_settings.serialize_json(value)
    return out


def deserialize_json(data: dict) -> RouteSettingsMap:
    out: RouteSettingsMap = {}
    for key, value in data.items():
        import capo_apigatewayv2.types.route_settings

        out[key] = capo_apigatewayv2.types.route_settings.deserialize_json(value)
    return out
