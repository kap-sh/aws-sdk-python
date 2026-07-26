"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfApiStageThrottleSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.string
    import capo_api_gateway.types.throttle_settings

MapOfApiStageThrottleSettings: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.throttle_settings.ThrottleSettings",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfApiStageThrottleSettings) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.throttle_settings

        out[key] = capo_api_gateway.types.throttle_settings.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfApiStageThrottleSettings:
    out: MapOfApiStageThrottleSettings = {}
    for key, value in data.items():
        import capo_api_gateway.types.throttle_settings

        out[key] = capo_api_gateway.types.throttle_settings.deserialize_json(value)
    return out
