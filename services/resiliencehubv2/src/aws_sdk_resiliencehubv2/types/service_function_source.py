"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionSource``."""

from typing import Literal, TypeAlias, cast

ServiceFunctionSource: TypeAlias = Literal[
    "AI_GENERATED",
    "USER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunctionSource) -> str:
    return value


def deserialize_json(data: str) -> ServiceFunctionSource:
    return cast(ServiceFunctionSource, data)
