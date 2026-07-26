"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SupportedApps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.supported_app

SupportedApps: TypeAlias = list["capo_socialmessaging.types.supported_app.SupportedApp"]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedApps) -> list:
    import capo_socialmessaging.types.supported_app

    out: list = []
    for item in value:
        out.append(capo_socialmessaging.types.supported_app.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedApps:
    import capo_socialmessaging.types.supported_app

    out: SupportedApps = []
    for item in data:
        out.append(capo_socialmessaging.types.supported_app.deserialize_json(item))
    return out
