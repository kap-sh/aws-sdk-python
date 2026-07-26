"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfMethodSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.method_setting
    import capo_api_gateway.types.string

MapOfMethodSettings: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.method_setting.MethodSetting",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfMethodSettings) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.method_setting

        out[key] = capo_api_gateway.types.method_setting.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfMethodSettings:
    out: MapOfMethodSettings = {}
    for key, value in data.items():
        import capo_api_gateway.types.method_setting

        out[key] = capo_api_gateway.types.method_setting.deserialize_json(value)
    return out
