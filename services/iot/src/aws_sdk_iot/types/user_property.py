"""Generated from Smithy shape ``com.amazonaws.iot#UserProperty``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.user_property_key
    import aws_sdk_iot.types.user_property_value


class UserProperty(TypedDict):
    key: "aws_sdk_iot.types.user_property_key.UserPropertyKey"
    """<p>A key to be specified in <code>UserProperty</code>.</p>"""
    value: "aws_sdk_iot.types.user_property_value.UserPropertyValue"
    """<p>A value to be specified in <code>UserProperty</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserProperty) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UserProperty:
    out: UserProperty = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("UserProperty.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("UserProperty.value required")
    return out
