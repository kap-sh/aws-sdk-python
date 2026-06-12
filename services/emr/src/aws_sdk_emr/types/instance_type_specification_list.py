"""Generated from Smithy shape ``com.amazonaws.emr#InstanceTypeSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_type_specification

InstanceTypeSpecificationList: TypeAlias = list[
    "aws_sdk_emr.types.instance_type_specification.InstanceTypeSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceTypeSpecificationList) -> list:
    import aws_sdk_emr.types.instance_type_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr.types.instance_type_specification.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceTypeSpecificationList:
    import aws_sdk_emr.types.instance_type_specification

    out: InstanceTypeSpecificationList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.instance_type_specification.deserialize_aws_json_1_1(item)
        )
    return out
