"""Generated from Smithy shape ``com.amazonaws.batch#AssignPublicIp``."""

from typing import Literal, TypeAlias, cast

AssignPublicIp: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssignPublicIp) -> str:
    return value


def deserialize_json(data: str) -> AssignPublicIp:
    return cast(AssignPublicIp, data)
