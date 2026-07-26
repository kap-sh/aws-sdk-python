"""Generated from Smithy shape ``com.amazonaws.batch#PlatformCapability``."""

from typing import Literal, TypeAlias, cast

PlatformCapability: TypeAlias = Literal[
    "EC2",
    "FARGATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PlatformCapability) -> str:
    return value


def deserialize_json(data: str) -> PlatformCapability:
    return cast(PlatformCapability, data)
