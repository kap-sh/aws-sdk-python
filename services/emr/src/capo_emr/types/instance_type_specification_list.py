"""Generated from Smithy shape ``com.amazonaws.emr#InstanceTypeSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance_type_specification

InstanceTypeSpecificationList: TypeAlias = list[
    "capo_emr.types.instance_type_specification.InstanceTypeSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceTypeSpecificationList) -> list:
    import capo_emr.types.instance_type_specification

    out: list = []
    for item in value:
        out.append(
            capo_emr.types.instance_type_specification.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceTypeSpecificationList:
    import capo_emr.types.instance_type_specification

    out: InstanceTypeSpecificationList = []
    for item in data:
        out.append(
            capo_emr.types.instance_type_specification.deserialize_aws_json_1_1(item)
        )
    return out
