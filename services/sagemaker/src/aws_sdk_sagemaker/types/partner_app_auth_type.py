"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppAuthType``."""

from typing import Literal, TypeAlias, cast

PartnerAppAuthType: TypeAlias = Literal["IAM",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppAuthType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerAppAuthType:
    return cast(PartnerAppAuthType, data)
