"""Generated from Smithy shape ``com.amazonaws.kafka#TargetCompressionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of compression to use producing records to the target cluster.</p>"""
TargetCompressionType: TypeAlias = Literal[
    "NONE",
    "GZIP",
    "SNAPPY",
    "LZ4",
    "ZSTD",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetCompressionType) -> str:
    return value


def deserialize_json(data: str) -> TargetCompressionType:
    return cast(TargetCompressionType, data)
