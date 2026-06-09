"""Generated from Smithy shape ``com.amazonaws.kms#OriginType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

OriginType: TypeAlias = Literal[
    "AWS_KMS",
    "EXTERNAL",
    "AWS_CLOUDHSM",
    "EXTERNAL_KEY_STORE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_KMS",
        "EXTERNAL",
        "AWS_CLOUDHSM",
        "EXTERNAL_KEY_STORE",
    )
)


def serialize_aws_json_1_1(value: OriginType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginType value: {data!r}")
    return cast(OriginType, data)
