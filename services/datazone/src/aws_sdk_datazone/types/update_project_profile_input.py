"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateProjectProfileInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_configurations_list
    import aws_sdk_datazone.types.project_profile_id
    import aws_sdk_datazone.types.project_profile_name
    import aws_sdk_datazone.types.project_resource_tag_parameters
    import aws_sdk_datazone.types.status


class UpdateProjectProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where a project profile is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
    """<p>The ID of a project profile that is to be updated.</p>"""
    name: NotRequired["aws_sdk_datazone.types.project_profile_name.ProjectProfileName"]
    """<p>The name of a project profile.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of a project profile.</p>"""
    status: NotRequired["aws_sdk_datazone.types.status.Status"]
    """<p>The status of a project profile.</p>"""
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
    """<p>The environment configurations of a project profile.</p>"""
    domain_unit_identifier: NotRequired[
        "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the domain unit where a project profile is to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectProfileInput) -> dict:
    out: dict = {}
    if "name" in value:
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


def deserialize_json(data: dict) -> UpdateProjectProfileInput:
    out: UpdateProjectProfileInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
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
