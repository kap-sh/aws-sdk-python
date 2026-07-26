"""Generated from Smithy shape ``com.amazonaws.transfer#MapType``."""

from typing import Literal, TypeAlias, cast

MapType: TypeAlias = Literal[
    "FILE",
    "DIRECTORY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MapType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MapType:
    return cast(MapType, data)
