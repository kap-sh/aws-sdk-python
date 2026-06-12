"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryLineageStartArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.association_entity_arn

QueryLineageStartArns: TypeAlias = list[
    "aws_sdk_sagemaker.types.association_entity_arn.AssociationEntityArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryLineageStartArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueryLineageStartArns:
    return list(data)
