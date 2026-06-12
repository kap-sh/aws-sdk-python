"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

ParallelDataFormat: TypeAlias = Literal[
    "TSV",
    "CSV",
    "TMX",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TSV",
        "CSV",
        "TMX",
    )
)


def serialize_aws_json_1_1(value: ParallelDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParallelDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParallelDataFormat value: {data!r}")
    return cast(ParallelDataFormat, data)
