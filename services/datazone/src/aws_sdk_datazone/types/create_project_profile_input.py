"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectProfileInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_configurations_list
    import aws_sdk_datazone.types.project_profile_name
    import aws_sdk_datazone.types.project_resource_tag_parameters
    import aws_sdk_datazone.types.status


class CreateProjectProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>A domain ID of the project profile.</p>"""
    name: "aws_sdk_datazone.types.project_profile_name.ProjectProfileName"
    """<p>Project profile name.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>A description of a project profile.</p>"""
    status: NotRequired["aws_sdk_datazone.types.status.Status"]
    """<p>Project profile status.</p>"""
    project_resource_tags: NotRequired[
        "aws_sdk_datazone.types.project_resource_tag_parameters.ProjectResourceTagParameters"
    ]
    """<p>The resource tags of the project profile.</p>"""
    allow_custom_project_resource_tags: NotRequired["bool"]
    """<p>Specifies whether custom project resource tags are supported.</p>"""
    project_resource_tags_description: NotRequired[
        "aws_sdk_datazone.types.description.Description"
    ]
    """<p>Field viewable through the UI that provides a project user with the allowed resource tag specifications.</p>"""
    environment_configurations: NotRequired[
        "aws_sdk_datazone.types.environment_configurations_list.EnvironmentConfigurationsList"
    ]
    """<p>Environment configurations of the project profile.</p>"""
    domain_unit_identifier: NotRequired[
        "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>A domain unit ID of the project profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectProfileInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.status

        out["status"] = aws_sdk_datazone.types.status.serialize_json(value["status"])
    if "project_resource_tags" in value:
        import aws_sdk_datazone.types.project_resource_tag_parameters

        out["projectResourceTags"] = (
            aws_sdk_datazone.types.project_resource_tag_parameters.serialize_json(
                value["project_resource_tags"]
            )
        )
    if "allow_custom_project_resource_tags" in value:
        out["allowCustomProjectResourceTags"] = value[
            "allow_custom_project_resource_tags"
        ]
    if "project_resource_tags_description" in value:
        out["projectResourceTagsDescription"] = value[
            "project_resource_tags_description"
        ]
    if "environment_configurations" in value:
        import aws_sdk_datazone.types.environment_configurations_list

        out["environmentConfigurations"] = (
            aws_sdk_datazone.types.environment_configurations_list.serialize_json(
                value["environment_configurations"]
            )
        )
    if "domain_unit_identifier" in value:
        out["domainUnitIdentifier"] = value["domain_unit_identifier"]
    return out


def deserialize_json(data: dict) -> CreateProjectProfileInput:
    out: CreateProjectProfileInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProjectProfileInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.status

        out["status"] = aws_sdk_datazone.types.status.deserialize_json(data["status"])
    if "projectResourceTags" in data:
        import aws_sdk_datazone.types.project_resource_tag_parameters

        out["project_resource_tags"] = (
            aws_sdk_datazone.types.project_resource_tag_parameters.deserialize_json(
                data["projectResourceTags"]
            )
        )
    if "allowCustomProjectResourceTags" in data:
        out["allow_custom_project_resource_tags"] = data[
            "allowCustomProjectResourceTags"
        ]
    if "projectResourceTagsDescription" in data:
        out["project_resource_tags_description"] = data[
            "projectResourceTagsDescription"
        ]
    if "environmentConfigurations" in data:
        import aws_sdk_datazone.types.environment_configurations_list

        out["environment_configurations"] = (
            aws_sdk_datazone.types.environment_configurations_list.deserialize_json(
                data["environmentConfigurations"]
            )
        )
    if "domainUnitIdentifier" in data:
        out["domain_unit_identifier"] = data["domainUnitIdentifier"]
    return out
