"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoreType``."""

from typing import Literal, TypeAlias, cast

CustomKeyStoreType: TypeAlias = Literal[
    "AWS_CLOUDHSM",
    "EXTERNAL_KEY_STORE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomKeyStoreType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomKeyStoreType:
    return cast(CustomKeyStoreType, data)
