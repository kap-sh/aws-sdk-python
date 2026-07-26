"""Generated from Smithy shape ``com.amazonaws.apigateway#CacheClusterSize``."""

from typing import Literal, TypeAlias, cast

"""<p>Returns the size of the CacheCluster.</p>"""
CacheClusterSize: TypeAlias = Literal[
    "0.5",
    "1.6",
    "6.1",
    "13.5",
    "28.4",
    "58.2",
    "118",
    "237",
]


# --- restJson1 ser/de ---
def serialize_json(value: CacheClusterSize) -> str:
    return value


def deserialize_json(data: str) -> CacheClusterSize:
    return cast(CacheClusterSize, data)
