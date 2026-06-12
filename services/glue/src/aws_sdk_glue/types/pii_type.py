"""Generated from Smithy shape ``com.amazonaws.glue#PiiType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

PiiType: TypeAlias = Literal[
    "RowAudit",
    "RowHashing",
    "RowMasking",
    "RowPartialMasking",
    "ColumnAudit",
    "ColumnHashing",
    "ColumnMasking",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RowAudit",
        "RowHashing",
        "RowMasking",
        "RowPartialMasking",
        "ColumnAudit",
        "ColumnHashing",
        "ColumnMasking",
    )
)


def serialize_aws_json_1_1(value: PiiType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PiiType value: {data!r}")
    return cast(PiiType, data)
