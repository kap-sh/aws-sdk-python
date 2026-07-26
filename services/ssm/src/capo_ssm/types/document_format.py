"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentFormat``."""

from typing import Literal, TypeAlias, cast

DocumentFormat: TypeAlias = Literal[
    "YAML",
    "JSON",
    "TEXT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentFormat:
    return cast(DocumentFormat, data)
