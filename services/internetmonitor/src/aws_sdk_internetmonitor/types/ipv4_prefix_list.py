"""Generated from Smithy shape ``com.amazonaws.internetmonitor#Ipv4PrefixList``."""

from typing import TypeAlias

Ipv4PrefixList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Ipv4PrefixList) -> list:
    return list(value)


def deserialize_json(data: list) -> Ipv4PrefixList:
    return list(data)
