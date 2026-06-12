"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationFilterValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_information_filter_value

InstanceInformationFilterValueSet: TypeAlias = list[
    "aws_sdk_ssm.types.instance_information_filter_value.InstanceInformationFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationFilterValueSet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceInformationFilterValueSet:
    return list(data)
