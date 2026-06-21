"""Generated from Smithy shape ``com.amazonaws.swf#ChildPolicy``."""

from typing import Literal, TypeAlias, cast

ChildPolicy: TypeAlias = Literal[
    "TERMINATE",
    "REQUEST_CANCEL",
    "ABANDON",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChildPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ChildPolicy:
    return cast(ChildPolicy, data)
