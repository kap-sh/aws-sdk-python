"""Generated from Smithy shape ``com.amazonaws.b2bi#TransformerStatus``."""

from typing import Literal, TypeAlias, cast

TransformerStatus: TypeAlias = Literal[
    "active",
    "inactive",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransformerStatus:
    return cast(TransformerStatus, data)
