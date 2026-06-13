"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#FormatOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

FormatOption: TypeAlias = Literal[
    "TEXT_OR_CSV",
    "PARQUET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT_OR_CSV",
        "PARQUET",
    )
)


def serialize_aws_json_1_1(value: FormatOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FormatOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FormatOption value: {data!r}")
    return cast(FormatOption, data)
