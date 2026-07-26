"""Generated from Smithy shape ``com.amazonaws.appconfig#ParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.extension_or_parameter_name
    import capo_appconfig.types.parameter

ParameterMap: TypeAlias = dict[
    "capo_appconfig.types.extension_or_parameter_name.ExtensionOrParameterName",
    "capo_appconfig.types.parameter.Parameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appconfig.types.parameter

        out[key] = capo_appconfig.types.parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ParameterMap:
    out: ParameterMap = {}
    for key, value in data.items():
        import capo_appconfig.types.parameter

        out[key] = capo_appconfig.types.parameter.deserialize_json(value)
    return out
