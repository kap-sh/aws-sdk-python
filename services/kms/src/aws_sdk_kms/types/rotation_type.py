"""Generated from Smithy shape ``com.amazonaws.kms#RotationType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

RotationType: TypeAlias = Literal[
    "AUTOMATIC",
    "ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "ON_DEMAND",
    )
)


def serialize_aws_json_1_1(value: RotationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RotationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RotationType value: {data!r}")
    return cast(RotationType, data)
