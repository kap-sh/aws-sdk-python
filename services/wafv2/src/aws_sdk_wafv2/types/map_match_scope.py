"""Generated from Smithy shape ``com.amazonaws.wafv2#MapMatchScope``."""

from typing import Literal, TypeAlias, cast

MapMatchScope: TypeAlias = Literal[
    "ALL",
    "KEY",
    "VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MapMatchScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MapMatchScope:
    return cast(MapMatchScope, data)
