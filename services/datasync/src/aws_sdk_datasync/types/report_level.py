"""Generated from Smithy shape ``com.amazonaws.datasync#ReportLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ReportLevel: TypeAlias = Literal[
    "ERRORS_ONLY",
    "SUCCESSES_AND_ERRORS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERRORS_ONLY",
        "SUCCESSES_AND_ERRORS",
    )
)


def serialize_aws_json_1_1(value: ReportLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportLevel value: {data!r}")
    return cast(ReportLevel, data)
