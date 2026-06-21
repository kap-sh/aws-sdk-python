"""Generated from Smithy shape ``com.amazonaws.sagemaker#TableFormat``."""

from typing import Literal, TypeAlias, cast

TableFormat: TypeAlias = Literal[
    "Default",
    "Glue",
    "Iceberg",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableFormat:
    return cast(TableFormat, data)
