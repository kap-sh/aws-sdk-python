"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Members``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.identity

Members: TypeAlias = list["aws_sdk_chime_sdk_messaging.types.identity.Identity"]


# --- restJson1 ser/de ---
def serialize_json(value: Members) -> list:
    import aws_sdk_chime_sdk_messaging.types.identity

    out: list = []
    for item in value:
        out.append(aws_sdk_chime_sdk_messaging.types.identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> Members:
    import aws_sdk_chime_sdk_messaging.types.identity

    out: Members = []
    for item in data:
        out.append(aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(item))
    return out
