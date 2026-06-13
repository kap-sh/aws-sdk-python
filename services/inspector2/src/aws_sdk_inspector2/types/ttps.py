"""Generated from Smithy shape ``com.amazonaws.inspector2#Ttps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ttp

Ttps: TypeAlias = list["aws_sdk_inspector2.types.ttp.Ttp"]


# --- restJson1 ser/de ---
def serialize_json(value: Ttps) -> list:
    return list(value)


def deserialize_json(data: list) -> Ttps:
    return list(data)
