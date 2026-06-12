"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_property_filter_value

InstancePropertyFilterValueSet: TypeAlias = list[
    "aws_sdk_ssm.types.instance_property_filter_value.InstancePropertyFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyFilterValueSet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstancePropertyFilterValueSet:
    return list(data)
