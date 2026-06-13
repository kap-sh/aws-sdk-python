"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#S3OutputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

S3OutputType: TypeAlias = Literal[
    "CUSTOM",
    "ATHENA",
    "REDSHIFT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "ATHENA",
        "REDSHIFT",
    )
)


def serialize_aws_json_1_1(value: S3OutputType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3OutputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3OutputType value: {data!r}")
    return cast(S3OutputType, data)
