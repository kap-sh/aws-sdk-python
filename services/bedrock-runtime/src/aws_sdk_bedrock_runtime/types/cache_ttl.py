"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CacheTTL``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

"""<p>Time-to-live duration for ephemeral cache entries</p>"""
CacheTTL: TypeAlias = Literal[
    "5m",
    "1h",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "5m",
        "1h",
    )
)


def serialize_json(value: CacheTTL) -> str:
    return value


def deserialize_json(data: str) -> CacheTTL:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheTTL value: {data!r}")
    return cast(CacheTTL, data)
