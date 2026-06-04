"""Generated from Smithy shape ``com.amazonaws.ecs#EBSTagSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ebs_tag_specification

EBSTagSpecifications: TypeAlias = list[
    "aws_sdk_ecs.types.ebs_tag_specification.EBSTagSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EBSTagSpecifications) -> list:
    import aws_sdk_ecs.types.ebs_tag_specification

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.ebs_tag_specification.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EBSTagSpecifications:
    import aws_sdk_ecs.types.ebs_tag_specification

    out: EBSTagSpecifications = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.ebs_tag_specification.deserialize_aws_json_1_1(item)
        )
    return out
