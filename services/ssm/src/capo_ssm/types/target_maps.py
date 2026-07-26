"""Generated from Smithy shape ``com.amazonaws.ssm#TargetMaps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.target_map

TargetMaps: TypeAlias = list["capo_ssm.types.target_map.TargetMap"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetMaps) -> list:
    import capo_ssm.types.target_map

    out: list = []
    for item in value:
        out.append(capo_ssm.types.target_map.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetMaps:
    import capo_ssm.types.target_map

    out: TargetMaps = []
    for item in data:
        out.append(capo_ssm.types.target_map.deserialize_aws_json_1_1(item))
    return out
