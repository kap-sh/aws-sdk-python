"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListUpdateMode``."""

from typing import Literal, TypeAlias, cast

ListUpdateMode: TypeAlias = Literal[
    "REPLACE",
    "APPEND",
    "REMOVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUpdateMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListUpdateMode:
    return cast(ListUpdateMode, data)
