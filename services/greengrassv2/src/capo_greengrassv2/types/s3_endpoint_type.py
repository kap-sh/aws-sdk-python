"""Generated from Smithy shape ``com.amazonaws.greengrassv2#S3EndpointType``."""

from typing import Literal, TypeAlias, cast

S3EndpointType: TypeAlias = Literal[
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3EndpointType) -> str:
    return value


def deserialize_json(data: str) -> S3EndpointType:
    return cast(S3EndpointType, data)
