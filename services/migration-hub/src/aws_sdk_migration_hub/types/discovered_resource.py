"""Generated from Smithy shape ``com.amazonaws.migrationhub#DiscoveredResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.configuration_id
    import aws_sdk_migration_hub.types.discovered_resource_description


class DiscoveredResource(TypedDict):
    configuration_id: "aws_sdk_migration_hub.types.configuration_id.ConfigurationId"
    """<p>The configurationId in Application Discovery Service that uniquely identifies the on-premise resource.</p>"""
    description: NotRequired[
        "aws_sdk_migration_hub.types.discovered_resource_description.DiscoveredResourceDescription"
    ]
    """<p>A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResource) -> dict:
    out: dict = {}
    out["ConfigurationId"] = value["configuration_id"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoveredResource:
    out: DiscoveredResource = {}  # type: ignore[typeddict-item]
    if "ConfigurationId" in data:
        out["configuration_id"] = data["ConfigurationId"]
    else:
        raise DeserializationError("DiscoveredResource.configuration_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
