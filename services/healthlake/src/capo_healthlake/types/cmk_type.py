"""Generated from Smithy shape ``com.amazonaws.healthlake#CmkType``."""

from typing import Literal, TypeAlias, cast

CmkType: TypeAlias = Literal[
    "CUSTOMER_MANAGED_KMS_KEY",
    "AWS_OWNED_KMS_KEY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CmkType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CmkType:
    return cast(CmkType, data)
