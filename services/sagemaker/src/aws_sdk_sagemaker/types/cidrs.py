"""Generated from Smithy shape ``com.amazonaws.sagemaker#Cidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cidr

Cidrs: TypeAlias = list["aws_sdk_sagemaker.types.cidr.Cidr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cidrs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Cidrs:
    return list(data)
