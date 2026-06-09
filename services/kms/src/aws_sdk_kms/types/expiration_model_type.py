"""Generated from Smithy shape ``com.amazonaws.kms#ExpirationModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

ExpirationModelType: TypeAlias = Literal[
    "KEY_MATERIAL_EXPIRES",
    "KEY_MATERIAL_DOES_NOT_EXPIRE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY_MATERIAL_EXPIRES",
        "KEY_MATERIAL_DOES_NOT_EXPIRE",
    )
)


def serialize_aws_json_1_1(value: ExpirationModelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpirationModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExpirationModelType value: {data!r}")
    return cast(ExpirationModelType, data)
