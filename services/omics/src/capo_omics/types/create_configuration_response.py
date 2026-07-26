"""Generated from Smithy shape ``com.amazonaws.omics#CreateConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.configuration_arn
    import capo_omics.types.configuration_description
    import capo_omics.types.configuration_name
    import capo_omics.types.configuration_status
    import capo_omics.types.configuration_timestamp
    import capo_omics.types.configuration_uuid
    import capo_omics.types.run_configurations_response
    import capo_omics.types.tag_map


class CreateConfigurationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.configuration_arn.ConfigurationArn"]
    """<p>Unique resource identifier for the configuration.</p>"""
    uuid: NotRequired["capo_omics.types.configuration_uuid.ConfigurationUuid"]
    """<p>Unique identifier for the configuration.</p>"""
    name: NotRequired["capo_omics.types.configuration_name.ConfigurationName"]
    """<p>User-friendly name for the configuration.</p>"""
    description: NotRequired[
        "capo_omics.types.configuration_description.ConfigurationDescription"
    ]
    """<p>Description for the configuration.</p>"""
    run_configurations: NotRequired[
        "capo_omics.types.run_configurations_response.RunConfigurationsResponse"
    ]
    """<p>Run-specific configurations.</p>"""
    status: NotRequired["capo_omics.types.configuration_status.ConfigurationStatus"]
    """<p>Current configuration status.</p>"""
    creation_time: NotRequired[
        "capo_omics.types.configuration_timestamp.ConfigurationTimestamp"
    ]
    """<p>Configuration creation timestamp.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Tags for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "run_configurations" in value:
        import capo_omics.types.run_configurations_response

        out["runConfigurations"] = (
            capo_omics.types.run_configurations_response.serialize_json(
                value["run_configurations"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import capo_omics.types.configuration_timestamp

        out["creationTime"] = capo_omics.types.configuration_timestamp.serialize_json(
            value["creation_time"]
        )
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationResponse:
    out: CreateConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "runConfigurations" in data:
        import capo_omics.types.run_configurations_response

        out["run_configurations"] = (
            capo_omics.types.run_configurations_response.deserialize_json(
                data["runConfigurations"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "creationTime" in data:
        import capo_omics.types.configuration_timestamp

        out["creation_time"] = (
            capo_omics.types.configuration_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    return out
