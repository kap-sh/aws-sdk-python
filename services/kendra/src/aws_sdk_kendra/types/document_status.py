"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

DocumentStatus: TypeAlias = Literal[
    "NOT_FOUND",
    "PROCESSING",
    "INDEXED",
    "UPDATED",
    "FAILED",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentStatus:
    return cast(DocumentStatus, data)
