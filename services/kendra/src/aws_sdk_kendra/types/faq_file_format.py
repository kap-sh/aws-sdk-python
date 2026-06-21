"""Generated from Smithy shape ``com.amazonaws.kendra#FaqFileFormat``."""

from typing import Literal, TypeAlias, cast

FaqFileFormat: TypeAlias = Literal[
    "CSV",
    "CSV_WITH_HEADER",
    "JSON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqFileFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaqFileFormat:
    return cast(FaqFileFormat, data)
