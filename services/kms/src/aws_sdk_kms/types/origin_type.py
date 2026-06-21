"""Generated from Smithy shape ``com.amazonaws.kms#OriginType``."""

from typing import Literal, TypeAlias, cast

OriginType: TypeAlias = Literal[
    "AWS_KMS",
    "EXTERNAL",
    "AWS_CLOUDHSM",
    "EXTERNAL_KEY_STORE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OriginType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginType:
    return cast(OriginType, data)
