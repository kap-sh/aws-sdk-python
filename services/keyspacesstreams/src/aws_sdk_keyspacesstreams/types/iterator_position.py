"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#IteratorPosition``."""

from typing import Literal, TypeAlias, cast

IteratorPosition: TypeAlias = Literal[
    "AT_TIP",
    "BEHIND_TIP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IteratorPosition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IteratorPosition:
    return cast(IteratorPosition, data)
