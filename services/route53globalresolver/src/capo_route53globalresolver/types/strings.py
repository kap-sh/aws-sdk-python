"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#Strings``."""

from typing import TypeAlias

Strings: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Strings) -> list:
    return list(value)


def deserialize_json(data: list) -> Strings:
    return list(data)
