"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#EdnsClientSubnetType``."""

from typing import Literal, TypeAlias, cast

EdnsClientSubnetType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EdnsClientSubnetType) -> str:
    return value


def deserialize_json(data: str) -> EdnsClientSubnetType:
    return cast(EdnsClientSubnetType, data)
