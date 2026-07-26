"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OriginationRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.origination_route

OriginationRouteList: TypeAlias = list[
    "capo_chime_sdk_voice.types.origination_route.OriginationRoute"
]


# --- restJson1 ser/de ---
def serialize_json(value: OriginationRouteList) -> list:
    import capo_chime_sdk_voice.types.origination_route

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.origination_route.serialize_json(item))
    return out


def deserialize_json(data: list) -> OriginationRouteList:
    import capo_chime_sdk_voice.types.origination_route

    out: OriginationRouteList = []
    for item in data:
        out.append(capo_chime_sdk_voice.types.origination_route.deserialize_json(item))
    return out
