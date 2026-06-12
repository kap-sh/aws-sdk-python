"""Generated from Smithy shape ``com.amazonaws.glue#DdbExportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DdbExportType: TypeAlias = Literal[
    "ddb",
    "s3",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ddb",
        "s3",
    )
)


def serialize_aws_json_1_1(value: DdbExportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DdbExportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DdbExportType value: {data!r}")
    return cast(DdbExportType, data)
