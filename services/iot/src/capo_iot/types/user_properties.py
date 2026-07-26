"""Generated from Smithy shape ``com.amazonaws.iot#UserProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.user_property

UserProperties: TypeAlias = list["capo_iot.types.user_property.UserProperty"]


# --- restJson1 ser/de ---
def serialize_json(value: UserProperties) -> list:
    import capo_iot.types.user_property

    out: list = []
    for item in value:
        out.append(capo_iot.types.user_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserProperties:
    import capo_iot.types.user_property

    out: UserProperties = []
    for item in data:
        out.append(capo_iot.types.user_property.deserialize_json(item))
    return out
