"""Generated from Smithy shape ``com.amazonaws.iot#ThingTypeProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.mqtt5_configuration
    import aws_sdk_iot.types.searchable_attributes
    import aws_sdk_iot.types.thing_type_description


class ThingTypeProperties(TypedDict):
    thing_type_description: NotRequired[
        "aws_sdk_iot.types.thing_type_description.ThingTypeDescription"
    ]
    """<p>The description of the thing type.</p>"""
    searchable_attributes: NotRequired[
        "aws_sdk_iot.types.searchable_attributes.SearchableAttributes"
    ]
    """<p>A list of searchable thing attribute names.</p>"""
    mqtt5_configuration: NotRequired[
        "aws_sdk_iot.types.mqtt5_configuration.Mqtt5Configuration"
    ]
    """<p>The configuration to add user-defined properties to enrich MQTT 5 messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingTypeProperties) -> dict:
    out: dict = {}
    if "thing_type_description" in value:
        out["thingTypeDescription"] = value["thing_type_description"]
    if "searchable_attributes" in value:
        import aws_sdk_iot.types.searchable_attributes

        out["searchableAttributes"] = (
            aws_sdk_iot.types.searchable_attributes.serialize_json(
                value["searchable_attributes"]
            )
        )
    if "mqtt5_configuration" in value:
        import aws_sdk_iot.types.mqtt5_configuration

        out["mqtt5Configuration"] = (
            aws_sdk_iot.types.mqtt5_configuration.serialize_json(
                value["mqtt5_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThingTypeProperties:
    out: ThingTypeProperties = {}  # type: ignore[typeddict-item]
    if "thingTypeDescription" in data:
        out["thing_type_description"] = data["thingTypeDescription"]
    if "searchableAttributes" in data:
        import aws_sdk_iot.types.searchable_attributes

        out["searchable_attributes"] = (
            aws_sdk_iot.types.searchable_attributes.deserialize_json(
                data["searchableAttributes"]
            )
        )
    if "mqtt5Configuration" in data:
        import aws_sdk_iot.types.mqtt5_configuration

        out["mqtt5_configuration"] = (
            aws_sdk_iot.types.mqtt5_configuration.deserialize_json(
                data["mqtt5Configuration"]
            )
        )
    return out
