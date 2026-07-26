"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaEventSourceType``."""

from typing import Literal, TypeAlias, cast

LambdaEventSourceType: TypeAlias = Literal[
    "PUB_SUB",
    "IOT_CORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaEventSourceType) -> str:
    return value


def deserialize_json(data: str) -> LambdaEventSourceType:
    return cast(LambdaEventSourceType, data)
