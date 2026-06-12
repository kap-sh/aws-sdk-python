"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

TerminologyDataFormat: TypeAlias = Literal[
    "CSV",
    "TMX",
    "TSV",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "TMX",
        "TSV",
    )
)


def serialize_aws_json_1_1(value: TerminologyDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TerminologyDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TerminologyDataFormat value: {data!r}")
    return cast(TerminologyDataFormat, data)
