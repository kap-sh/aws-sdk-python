"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RegionMapInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.region_map_input_value
    import aws_sdk_ssm_incidents.types.region_name

RegionMapInput: TypeAlias = dict[
    "aws_sdk_ssm_incidents.types.region_name.RegionName",
    "aws_sdk_ssm_incidents.types.region_map_input_value.RegionMapInputValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RegionMapInput) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm_incidents.types.region_map_input_value

        out[key] = aws_sdk_ssm_incidents.types.region_map_input_value.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> RegionMapInput:
    out: RegionMapInput = {}
    for key, value in data.items():
        import aws_sdk_ssm_incidents.types.region_map_input_value

        out[key] = aws_sdk_ssm_incidents.types.region_map_input_value.deserialize_json(
            value
        )
    return out
