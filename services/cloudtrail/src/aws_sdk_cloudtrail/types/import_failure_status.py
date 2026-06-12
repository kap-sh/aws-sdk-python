"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportFailureStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

ImportFailureStatus: TypeAlias = Literal[
    "FAILED",
    "RETRY",
    "SUCCEEDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "RETRY",
        "SUCCEEDED",
    )
)


def serialize_aws_json_1_1(value: ImportFailureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportFailureStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportFailureStatus value: {data!r}")
    return cast(ImportFailureStatus, data)
