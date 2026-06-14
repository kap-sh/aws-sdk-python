"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateProjectProfileOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_configurations_list
    import aws_sdk_datazone.types.project_profile_id
    import aws_sdk_datazone.types.project_profile_name
    import aws_sdk_datazone.types.project_resource_tag_parameters
    import aws_sdk_datazone.types.status


class UpdateProjectProfileOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where project profile is to be updated.</p>"""
    id: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
    """<p>The ID of the project profile.</p>"""
    name: "aws_sdk_datazone.types.project_profile_name.ProjectProfileName"
    """<p>The name of the project profile.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of a project profile.</p>"""
    status: NotRequired["aws_sdk_datazone.types.status.Status"]
    """<p>The status of the project profile.</p>"""
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
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The user who created a project profile.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which a project profile is created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which a project profile was last updated.</p>"""
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The domain unit ID of the project profile to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectProfileOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
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
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lastUpdatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    return out


def deserialize_json(data: dict) -> UpdateProjectProfileOutput:
    out: UpdateProjectProfileOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateProjectProfileOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateProjectProfileOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateProjectProfileOutput.name required")
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
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("UpdateProjectProfileOutput.created_by required")
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    return out
