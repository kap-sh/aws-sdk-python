"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name
    import capo_iotdeviceadvisor.types.suite_definition_configuration
    import capo_iotdeviceadvisor.types.suite_definition_version
    import capo_iotdeviceadvisor.types.tag_map
    import capo_iotdeviceadvisor.types.timestamp
    import capo_iotdeviceadvisor.types.uuid


class GetSuiteDefinitionResponse(TypedDict, closed=True):
    suite_definition_id: NotRequired["capo_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite definition ID of the suite definition.</p>"""
    suite_definition_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the suite definition.</p>"""
    suite_definition_version: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Suite definition version of the suite definition.</p>"""
    latest_version: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Latest suite definition version of the suite definition.</p>"""
    suite_definition_configuration: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration"
    ]
    """<p>Suite configuration of the suite definition.</p>"""
    created_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the suite definition was created.</p>"""
    last_modified_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the suite definition was last modified.</p>"""
    tags: NotRequired["capo_iotdeviceadvisor.types.tag_map.TagMap"]
    """<p>Tags attached to the suite definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuiteDefinitionResponse) -> dict:
    out: dict = {}
    if "suite_definition_id" in value:
        out["suiteDefinitionId"] = value["suite_definition_id"]
    if "suite_definition_arn" in value:
        out["suiteDefinitionArn"] = value["suite_definition_arn"]
    if "suite_definition_version" in value:
        out["suiteDefinitionVersion"] = value["suite_definition_version"]
    if "latest_version" in value:
        out["latestVersion"] = value["latest_version"]
    if "suite_definition_configuration" in value:
        import capo_iotdeviceadvisor.types.suite_definition_configuration

        out["suiteDefinitionConfiguration"] = (
            capo_iotdeviceadvisor.types.suite_definition_configuration.serialize_json(
                value["suite_definition_configuration"]
            )
        )
    if "created_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["createdAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["lastModifiedAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["last_modified_at"]
        )
    if "tags" in value:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSuiteDefinitionResponse:
    out: GetSuiteDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionId" in data:
        out["suite_definition_id"] = data["suiteDefinitionId"]
    if "suiteDefinitionArn" in data:
        out["suite_definition_arn"] = data["suiteDefinitionArn"]
    if "suiteDefinitionVersion" in data:
        out["suite_definition_version"] = data["suiteDefinitionVersion"]
    if "latestVersion" in data:
        out["latest_version"] = data["latestVersion"]
    if "suiteDefinitionConfiguration" in data:
        import capo_iotdeviceadvisor.types.suite_definition_configuration

        out["suite_definition_configuration"] = (
            capo_iotdeviceadvisor.types.suite_definition_configuration.deserialize_json(
                data["suiteDefinitionConfiguration"]
            )
        )
    if "createdAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["created_at"] = capo_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastModifiedAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["last_modified_at"] = (
            capo_iotdeviceadvisor.types.timestamp.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    if "tags" in data:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.deserialize_json(data["tags"])
    return out
