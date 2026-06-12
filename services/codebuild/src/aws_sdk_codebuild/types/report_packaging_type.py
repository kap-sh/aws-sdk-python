"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportPackagingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportPackagingType: TypeAlias = Literal[
    "ZIP",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZIP",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: ReportPackagingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportPackagingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportPackagingType value: {data!r}")
    return cast(ReportPackagingType, data)
