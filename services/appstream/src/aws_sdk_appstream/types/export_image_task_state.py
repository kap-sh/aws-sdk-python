"""Generated from Smithy shape ``com.amazonaws.appstream#ExportImageTaskState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ExportImageTaskState: TypeAlias = Literal[
    "EXPORTING",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPORTING",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_aws_json_1_1(value: ExportImageTaskState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportImageTaskState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportImageTaskState value: {data!r}")
    return cast(ExportImageTaskState, data)
