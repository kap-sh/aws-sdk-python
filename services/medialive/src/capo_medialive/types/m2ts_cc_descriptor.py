"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsCcDescriptor``."""

from typing import Literal, TypeAlias, cast

"""M2ts Cc Descriptor"""
M2tsCcDescriptor: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsCcDescriptor) -> str:
    return value


def deserialize_json(data: str) -> M2tsCcDescriptor:
    return cast(M2tsCcDescriptor, data)
