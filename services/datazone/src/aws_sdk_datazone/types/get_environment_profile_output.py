"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentProfileOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.custom_parameter_list
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.environment_profile_name
    import aws_sdk_datazone.types.project_id


class GetEnvironmentProfileOutput(TypedDict):
    id: "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    """<p>The ID of the environment profile.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this environment profile exists.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account where this environment profile exists.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region where this environment profile exists.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created this environment profile.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this environment profile was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this environment profile was upated.</p>"""
    name: "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
    """<p>The name of the environment profile.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the environment profile.</p>"""
    environment_blueprint_id: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The ID of the blueprint with which this environment profile is created.</p>"""
    project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the Amazon DataZone project in which this environment profile is created.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of the environment profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentProfileOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    if "user_parameters" in value:
        import aws_sdk_datazone.types.custom_parameter_list

        out["userParameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEnvironmentProfileOutput:
    out: GetEnvironmentProfileOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetEnvironmentProfileOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetEnvironmentProfileOutput.domain_id required")
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsAccountRegion" in data:
        out["aws_account_region"] = data["awsAccountRegion"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetEnvironmentProfileOutput.created_by required")
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updated_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetEnvironmentProfileOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "environmentBlueprintId" in data:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    else:
        raise DeserializationError(
            "GetEnvironmentProfileOutput.environment_blueprint_id required"
        )
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    if "userParameters" in data:
        import aws_sdk_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    return out
