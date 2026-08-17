"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_property_filter_value

InstancePropertyFilterValueSet: TypeAlias = list[
    "capo_ssm.types.instance_property_filter_value.InstancePropertyFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyFilterValueSet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstancePropertyFilterValueSet:
    return [item for item in data if item is not None]
