"""Generated from Smithy shape ``com.amazonaws.ssm#TargetValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.target_value

TargetValues: TypeAlias = list["capo_ssm.types.target_value.TargetValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetValues:
    return [item for item in data if item is not None]
