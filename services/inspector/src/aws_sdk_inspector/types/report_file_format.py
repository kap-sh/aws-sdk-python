"""Generated from Smithy shape ``com.amazonaws.inspector#ReportFileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

ReportFileFormat: TypeAlias = Literal[
    "HTML",
    "PDF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTML",
        "PDF",
    )
)


def serialize_aws_json_1_1(value: ReportFileFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportFileFormat value: {data!r}")
    return cast(ReportFileFormat, data)
