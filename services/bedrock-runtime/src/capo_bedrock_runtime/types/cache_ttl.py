"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CacheTTL``."""

from typing import Literal, TypeAlias, cast

"""<p>Time-to-live duration for ephemeral cache entries</p>"""
CacheTTL: TypeAlias = Literal[
    "5m",
    "1h",
]


# --- restJson1 ser/de ---
def serialize_json(value: CacheTTL) -> str:
    return value


def deserialize_json(data: str) -> CacheTTL:
    return cast(CacheTTL, data)
