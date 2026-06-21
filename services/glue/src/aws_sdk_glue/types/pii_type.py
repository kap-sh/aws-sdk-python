"""Generated from Smithy shape ``com.amazonaws.glue#PiiType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: PiiType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiType:
    return cast(PiiType, data)
