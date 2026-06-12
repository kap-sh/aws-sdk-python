"""Generated from Smithy shape ``com.amazonaws.iot#UserProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.user_property

UserProperties: TypeAlias = list["aws_sdk_iot.types.user_property.UserProperty"]


# --- restJson1 ser/de ---
def serialize_json(value: UserProperties) -> list:
    import aws_sdk_iot.types.user_property

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.user_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserProperties:
    import aws_sdk_iot.types.user_property

    out: UserProperties = []
    for item in data:
        out.append(aws_sdk_iot.types.user_property.deserialize_json(item))
    return out
