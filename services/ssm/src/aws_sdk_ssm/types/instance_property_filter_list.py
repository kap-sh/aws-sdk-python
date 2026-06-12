"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_property_filter

InstancePropertyFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.instance_property_filter.InstancePropertyFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyFilterList) -> list:
    import aws_sdk_ssm.types.instance_property_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.instance_property_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePropertyFilterList:
    import aws_sdk_ssm.types.instance_property_filter

    out: InstancePropertyFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.instance_property_filter.deserialize_aws_json_1_1(item)
        )
    return out
