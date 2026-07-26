"""Generated from Smithy shape ``com.amazonaws.ecs#EBSTagSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.ebs_tag_specification

EBSTagSpecifications: TypeAlias = list[
    "capo_ecs.types.ebs_tag_specification.EBSTagSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EBSTagSpecifications) -> list:
    import capo_ecs.types.ebs_tag_specification

    out: list = []
    for item in value:
        out.append(capo_ecs.types.ebs_tag_specification.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EBSTagSpecifications:
    import capo_ecs.types.ebs_tag_specification

    out: EBSTagSpecifications = []
    for item in data:
        out.append(capo_ecs.types.ebs_tag_specification.deserialize_aws_json_1_1(item))
    return out
