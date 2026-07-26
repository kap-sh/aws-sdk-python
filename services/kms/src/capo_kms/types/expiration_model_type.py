"""Generated from Smithy shape ``com.amazonaws.kms#ExpirationModelType``."""

from typing import Literal, TypeAlias, cast

ExpirationModelType: TypeAlias = Literal[
    "KEY_MATERIAL_EXPIRES",
    "KEY_MATERIAL_DOES_NOT_EXPIRE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpirationModelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpirationModelType:
    return cast(ExpirationModelType, data)
