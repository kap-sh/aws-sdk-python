"""Generated from Smithy shape ``com.amazonaws.sagemaker#AttributeNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.attribute_name

AttributeNames: TypeAlias = list["capo_sagemaker.types.attribute_name.AttributeName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AttributeNames:
    return list(data)
