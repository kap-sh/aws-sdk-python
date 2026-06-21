"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsPartition``."""

from typing import Literal, TypeAlias, cast

AwsPartition: TypeAlias = Literal["aws-eusc",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsPartition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsPartition:
    return cast(AwsPartition, data)
