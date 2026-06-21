"""Generated from Smithy shape ``com.amazonaws.finspace#dnsStatus``."""

from typing import Literal, TypeAlias, cast

dnsStatus: TypeAlias = Literal[
    "NONE",
    "UPDATE_REQUESTED",
    "UPDATING",
    "FAILED_UPDATE",
    "SUCCESSFULLY_UPDATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: dnsStatus) -> str:
    return value


def deserialize_json(data: str) -> dnsStatus:
    return cast(dnsStatus, data)
