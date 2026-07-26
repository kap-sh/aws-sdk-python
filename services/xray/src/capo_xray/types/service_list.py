"""Generated from Smithy shape ``com.amazonaws.xray#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.service

ServiceList: TypeAlias = list["capo_xray.types.service.Service"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceList) -> list:
    import capo_xray.types.service

    out: list = []
    for item in value:
        out.append(capo_xray.types.service.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceList:
    import capo_xray.types.service

    out: ServiceList = []
    for item in data:
        out.append(capo_xray.types.service.deserialize_json(item))
    return out
