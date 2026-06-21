"""Generated from Smithy shape ``com.amazonaws.glue#CsvSerdeOption``."""

from typing import Literal, TypeAlias, cast

CsvSerdeOption: TypeAlias = Literal[
    "OpenCSVSerDe",
    "LazySimpleSerDe",
    "None",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CsvSerdeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CsvSerdeOption:
    return cast(CsvSerdeOption, data)
