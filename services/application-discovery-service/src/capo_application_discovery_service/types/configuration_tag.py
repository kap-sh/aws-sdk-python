"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConfigurationTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configuration_id
    import capo_application_discovery_service.types.configuration_item_type
    import capo_application_discovery_service.types.tag_key
    import capo_application_discovery_service.types.tag_value
    import capo_application_discovery_service.types.time_stamp


class ConfigurationTag(TypedDict, closed=True):
    configuration_type: NotRequired[
        "capo_application_discovery_service.types.configuration_item_type.ConfigurationItemType"
    ]
    """<p>A type of IT asset to tag.</p>"""
    configuration_id: NotRequired[
        "capo_application_discovery_service.types.configuration_id.ConfigurationId"
    ]
    """<p>The configuration ID for the item to tag. You can specify a list of keys and values.</p>"""
    key: NotRequired["capo_application_discovery_service.types.tag_key.TagKey"]
    """<p>A type of tag on which to filter. For example, <i>serverType</i>.</p>"""
    value: NotRequired["capo_application_discovery_service.types.tag_value.TagValue"]
    """<p>A value on which to filter. For example <i>key = serverType</i> and <i>value = web server</i>.</p>"""
    time_of_creation: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The time the configuration tag was created in Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTag) -> dict:
    out: dict = {}
    if "configuration_type" in value:
        import capo_application_discovery_service.types.configuration_item_type

        out["configurationType"] = (
            capo_application_discovery_service.types.configuration_item_type.serialize_aws_json_1_1(
                value["configuration_type"]
            )
        )
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    if "time_of_creation" in value:
        import capo_application_discovery_service.types.time_stamp

        out["timeOfCreation"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["time_of_creation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationTag:
    out: ConfigurationTag = {}  # type: ignore[typeddict-item]
    if "configurationType" in data:
        import capo_application_discovery_service.types.configuration_item_type

        out["configuration_type"] = (
            capo_application_discovery_service.types.configuration_item_type.deserialize_aws_json_1_1(
                data["configurationType"]
            )
        )
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    if "timeOfCreation" in data:
        import capo_application_discovery_service.types.time_stamp

        out["time_of_creation"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["timeOfCreation"]
            )
        )
    return out
