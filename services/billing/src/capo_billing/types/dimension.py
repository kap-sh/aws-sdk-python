"""Generated from Smithy shape ``com.amazonaws.billing#Dimension``."""

from typing import Literal, TypeAlias, cast

Dimension: TypeAlias = Literal["LINKED_ACCOUNT",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    return cast(Dimension, data)
