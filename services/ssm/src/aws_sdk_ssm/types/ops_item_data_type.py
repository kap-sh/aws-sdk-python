"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemDataType``."""

from typing import Literal, TypeAlias, cast

OpsItemDataType: TypeAlias = Literal[
    "SearchableString",
    "String",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemDataType:
    return cast(OpsItemDataType, data)
