"""Generated from Smithy shape ``com.amazonaws.securityhub#Ranges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.range

Ranges: TypeAlias = list["capo_securityhub.types.range.Range"]


# --- restJson1 ser/de ---
def serialize_json(value: Ranges) -> list:
    import capo_securityhub.types.range

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.range.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ranges:
    import capo_securityhub.types.range

    out: Ranges = []
    for item in data:
        out.append(capo_securityhub.types.range.deserialize_json(item))
    return out
