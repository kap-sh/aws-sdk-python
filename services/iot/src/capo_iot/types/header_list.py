"""Generated from Smithy shape ``com.amazonaws.iot#HeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.http_action_header

HeaderList: TypeAlias = list["capo_iot.types.http_action_header.HttpActionHeader"]


# --- restJson1 ser/de ---
def serialize_json(value: HeaderList) -> list:
    import capo_iot.types.http_action_header

    out: list = []
    for item in value:
        out.append(capo_iot.types.http_action_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> HeaderList:
    import capo_iot.types.http_action_header

    out: HeaderList = []
    for item in data:
        out.append(capo_iot.types.http_action_header.deserialize_json(item))
    return out
