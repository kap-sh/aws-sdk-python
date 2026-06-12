"""Generated from Smithy shape ``com.amazonaws.pinpointemail#Esps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.esp

Esps: TypeAlias = list["aws_sdk_pinpoint_email.types.esp.Esp"]


# --- restJson1 ser/de ---
def serialize_json(value: Esps) -> list:
    return list(value)


def deserialize_json(data: list) -> Esps:
    return list(data)
