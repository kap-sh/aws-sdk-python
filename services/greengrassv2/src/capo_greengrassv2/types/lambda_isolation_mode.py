"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaIsolationMode``."""

from typing import Literal, TypeAlias, cast

LambdaIsolationMode: TypeAlias = Literal[
    "GreengrassContainer",
    "NoContainer",
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaIsolationMode) -> str:
    return value


def deserialize_json(data: str) -> LambdaIsolationMode:
    return cast(LambdaIsolationMode, data)
