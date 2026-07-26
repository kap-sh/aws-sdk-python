"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentParameterType``."""

from typing import Literal, TypeAlias, cast

DocumentParameterType: TypeAlias = Literal[
    "String",
    "StringList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentParameterType:
    return cast(DocumentParameterType, data)
