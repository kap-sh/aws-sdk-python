"""Generated from Smithy shape ``com.amazonaws.ssoadmin#KmsKeyType``."""

from typing import Literal, TypeAlias, cast

KmsKeyType: TypeAlias = Literal[
    "AWS_OWNED_KMS_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KmsKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KmsKeyType:
    return cast(KmsKeyType, data)
