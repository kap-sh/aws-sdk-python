"""Generated from Smithy shape ``com.amazonaws.securityagent#UriList``."""

from typing import TypeAlias

UriList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: UriList) -> list:
    return list(value)


def deserialize_json(data: list) -> UriList:
    return list(data)
