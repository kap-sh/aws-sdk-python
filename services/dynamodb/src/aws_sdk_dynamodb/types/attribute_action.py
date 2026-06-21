"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeAction``."""

from typing import Literal, TypeAlias, cast

AttributeAction: TypeAlias = Literal[
    "ADD",
    "PUT",
    "DELETE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AttributeAction:
    return cast(AttributeAction, data)
