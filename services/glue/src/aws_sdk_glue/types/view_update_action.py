"""Generated from Smithy shape ``com.amazonaws.glue#ViewUpdateAction``."""

from typing import Literal, TypeAlias, cast

ViewUpdateAction: TypeAlias = Literal[
    "ADD",
    "REPLACE",
    "ADD_OR_REPLACE",
    "DROP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewUpdateAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ViewUpdateAction:
    return cast(ViewUpdateAction, data)
