"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#Reboot``."""

from typing_extensions import TypedDict


class Reboot(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: Reboot) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> Reboot:
    out: Reboot = {}  # type: ignore[typeddict-item]
    return out
