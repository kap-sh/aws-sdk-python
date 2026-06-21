"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentFilterKey``."""

from typing import Literal, TypeAlias, cast

DocumentFilterKey: TypeAlias = Literal[
    "Name",
    "Owner",
    "PlatformTypes",
    "DocumentType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentFilterKey:
    return cast(DocumentFilterKey, data)
