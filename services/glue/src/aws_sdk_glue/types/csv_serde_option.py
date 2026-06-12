"""Generated from Smithy shape ``com.amazonaws.glue#CsvSerdeOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CsvSerdeOption: TypeAlias = Literal[
    "OpenCSVSerDe",
    "LazySimpleSerDe",
    "None",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OpenCSVSerDe",
        "LazySimpleSerDe",
        "None",
    )
)


def serialize_aws_json_1_1(value: CsvSerdeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CsvSerdeOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CsvSerdeOption value: {data!r}")
    return cast(CsvSerdeOption, data)
