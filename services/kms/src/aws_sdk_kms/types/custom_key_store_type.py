"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoreType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

CustomKeyStoreType: TypeAlias = Literal[
    "AWS_CLOUDHSM",
    "EXTERNAL_KEY_STORE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_CLOUDHSM",
        "EXTERNAL_KEY_STORE",
    )
)


def serialize_aws_json_1_1(value: CustomKeyStoreType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomKeyStoreType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomKeyStoreType value: {data!r}")
    return cast(CustomKeyStoreType, data)
