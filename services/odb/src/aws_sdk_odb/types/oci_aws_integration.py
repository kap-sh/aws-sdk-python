"""Generated from Smithy shape ``com.amazonaws.odb#OciAwsIntegration``."""

from typing import Literal, TypeAlias, cast

OciAwsIntegration: TypeAlias = Literal["KmsTde",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciAwsIntegration) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OciAwsIntegration:
    return cast(OciAwsIntegration, data)
