"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IncludeExclude``."""

from typing import Literal, TypeAlias, cast

IncludeExclude: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeExclude) -> str:
    return value


def deserialize_json(data: str) -> IncludeExclude:
    return cast(IncludeExclude, data)
