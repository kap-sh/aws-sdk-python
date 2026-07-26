"""Generated from Smithy shape ``com.amazonaws.iot#PropagatingAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.attribute_name
    import capo_iot.types.connection_attribute_name
    import capo_iot.types.user_property_key_name


class PropagatingAttribute(TypedDict, closed=True):
    user_property_key: NotRequired[
        "capo_iot.types.user_property_key_name.UserPropertyKeyName"
    ]
    """<p>The key of the user property key-value pair.</p>"""
    thing_attribute: NotRequired["capo_iot.types.attribute_name.AttributeName"]
    """<p>The user-defined thing attribute that is propagating for MQTT 5 message enrichment.</p>"""
    connection_attribute: NotRequired[
        "capo_iot.types.connection_attribute_name.ConnectionAttributeName"
    ]
    """<p>The attribute associated with the connection between a device and Amazon Web Services IoT Core.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropagatingAttribute) -> dict:
    out: dict = {}
    if "user_property_key" in value:
        out["userPropertyKey"] = value["user_property_key"]
    if "thing_attribute" in value:
        out["thingAttribute"] = value["thing_attribute"]
    if "connection_attribute" in value:
        out["connectionAttribute"] = value["connection_attribute"]
    return out


def deserialize_json(data: dict) -> PropagatingAttribute:
    out: PropagatingAttribute = {}  # type: ignore[typeddict-item]
    if "userPropertyKey" in data:
        out["user_property_key"] = data["userPropertyKey"]
    if "thingAttribute" in data:
        out["thing_attribute"] = data["thingAttribute"]
    if "connectionAttribute" in data:
        out["connection_attribute"] = data["connectionAttribute"]
    return out
