"""Generated from Smithy shape ``com.amazonaws.sesv2#Routes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.route

Routes: TypeAlias = list["capo_sesv2.types.route.Route"]


# --- restJson1 ser/de ---
def serialize_json(value: Routes) -> list:
    import capo_sesv2.types.route

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.route.serialize_json(item))
    return out


def deserialize_json(data: list) -> Routes:
    import capo_sesv2.types.route

    out: Routes = []
    for item in data:
        out.append(capo_sesv2.types.route.deserialize_json(item))
    return out
