"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#FormatOption``."""

from typing import Literal, TypeAlias, cast

FormatOption: TypeAlias = Literal[
    "TEXT_OR_CSV",
    "PARQUET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FormatOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FormatOption:
    return cast(FormatOption, data)
