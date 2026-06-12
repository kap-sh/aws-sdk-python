"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string40

QueryTypes: TypeAlias = list["aws_sdk_sagemaker.types.string40.String40"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueryTypes:
    return list(data)
