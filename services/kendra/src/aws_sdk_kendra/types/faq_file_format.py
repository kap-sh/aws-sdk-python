"""Generated from Smithy shape ``com.amazonaws.kendra#FaqFileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

FaqFileFormat: TypeAlias = Literal[
    "CSV",
    "CSV_WITH_HEADER",
    "JSON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "CSV_WITH_HEADER",
        "JSON",
    )
)


def serialize_aws_json_1_1(value: FaqFileFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaqFileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FaqFileFormat value: {data!r}")
    return cast(FaqFileFormat, data)
