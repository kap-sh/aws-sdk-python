"""Generated from Smithy shape ``com.amazonaws.datasync#VerifyMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

VerifyMode: TypeAlias = Literal[
    "POINT_IN_TIME_CONSISTENT",
    "ONLY_FILES_TRANSFERRED",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POINT_IN_TIME_CONSISTENT",
        "ONLY_FILES_TRANSFERRED",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: VerifyMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VerifyMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerifyMode value: {data!r}")
    return cast(VerifyMode, data)
