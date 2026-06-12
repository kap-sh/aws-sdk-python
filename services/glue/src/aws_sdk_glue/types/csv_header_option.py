"""Generated from Smithy shape ``com.amazonaws.glue#CsvHeaderOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CsvHeaderOption: TypeAlias = Literal[
    "UNKNOWN",
    "PRESENT",
    "ABSENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN",
        "PRESENT",
        "ABSENT",
    )
)


def serialize_aws_json_1_1(value: CsvHeaderOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CsvHeaderOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CsvHeaderOption value: {data!r}")
    return cast(CsvHeaderOption, data)
