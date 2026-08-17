"""Generated from Smithy shape ``com.amazonaws.ssm#TargetMapValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.target_map_value

TargetMapValueList: TypeAlias = list["capo_ssm.types.target_map_value.TargetMapValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetMapValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetMapValueList:
    return [item for item in data if item is not None]
