"""Generated from Smithy shape ``com.amazonaws.glue#CsvHeaderOption``."""

from typing import Literal, TypeAlias, cast

CsvHeaderOption: TypeAlias = Literal[
    "UNKNOWN",
    "PRESENT",
    "ABSENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CsvHeaderOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CsvHeaderOption:
    return cast(CsvHeaderOption, data)
