"""Generated from Smithy shape ``com.amazonaws.panorama#DnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.dns

DnsList: TypeAlias = list["aws_sdk_panorama.types.dns.Dns"]


# --- restJson1 ser/de ---
def serialize_json(value: DnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> DnsList:
    return list(data)
