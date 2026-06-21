"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataFieldDataType``."""

from typing import Literal, TypeAlias, cast

CodegenGenericDataFieldDataType: TypeAlias = Literal[
    "ID",
    "String",
    "Int",
    "Float",
    "AWSDate",
    "AWSTime",
    "AWSDateTime",
    "AWSTimestamp",
    "AWSEmail",
    "AWSURL",
    "AWSIPAddress",
    "Boolean",
    "AWSJSON",
    "AWSPhone",
    "Enum",
    "Model",
    "NonModel",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataFieldDataType) -> str:
    return value


def deserialize_json(data: str) -> CodegenGenericDataFieldDataType:
    return cast(CodegenGenericDataFieldDataType, data)
