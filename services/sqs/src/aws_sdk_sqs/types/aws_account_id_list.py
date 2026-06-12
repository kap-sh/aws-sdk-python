"""Generated from Smithy shape ``com.amazonaws.sqs#AWSAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string

AWSAccountIdList: TypeAlias = list["aws_sdk_sqs.types.string.String"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AWSAccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AWSAccountIdList:
    return list(data)
