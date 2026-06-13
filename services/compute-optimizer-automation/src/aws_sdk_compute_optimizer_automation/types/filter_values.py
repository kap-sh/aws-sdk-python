"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.filter_value

FilterValues: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.filter_value.FilterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FilterValues:
    return list(data)
