"""Generated from Smithy shape ``com.amazonaws.odb#SupportedAwsIntegration``."""

from typing import Literal, TypeAlias, cast

SupportedAwsIntegration: TypeAlias = Literal["KmsTde",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedAwsIntegration) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SupportedAwsIntegration:
    return cast(SupportedAwsIntegration, data)
