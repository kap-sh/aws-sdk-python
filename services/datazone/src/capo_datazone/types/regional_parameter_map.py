"""Generated from Smithy shape ``com.amazonaws.datazone#RegionalParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.region_name
    import capo_datazone.types.regional_parameter

RegionalParameterMap: TypeAlias = dict[
    "capo_datazone.types.region_name.RegionName",
    "capo_datazone.types.regional_parameter.RegionalParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RegionalParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_datazone.types.regional_parameter

        out[key] = capo_datazone.types.regional_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> RegionalParameterMap:
    out: RegionalParameterMap = {}
    for key, value in data.items():
        import capo_datazone.types.regional_parameter

        out[key] = capo_datazone.types.regional_parameter.deserialize_json(value)
    return out
