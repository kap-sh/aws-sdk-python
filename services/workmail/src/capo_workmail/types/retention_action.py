"""Generated from Smithy shape ``com.amazonaws.workmail#RetentionAction``."""

from typing import Literal, TypeAlias, cast

RetentionAction: TypeAlias = Literal[
    "NONE",
    "DELETE",
    "PERMANENTLY_DELETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionAction:
    return cast(RetentionAction, data)
