"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RegionInfoMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.region_info
    import aws_sdk_ssm_incidents.types.region_name

RegionInfoMap: TypeAlias = dict[
    "aws_sdk_ssm_incidents.types.region_name.RegionName",
    "aws_sdk_ssm_incidents.types.region_info.RegionInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RegionInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm_incidents.types.region_info

        out[key] = aws_sdk_ssm_incidents.types.region_info.serialize_json(value)
    return out


def deserialize_json(data: dict) -> RegionInfoMap:
    out: RegionInfoMap = {}
    for key, value in data.items():
        import aws_sdk_ssm_incidents.types.region_info

        out[key] = aws_sdk_ssm_incidents.types.region_info.deserialize_json(value)
    return out
