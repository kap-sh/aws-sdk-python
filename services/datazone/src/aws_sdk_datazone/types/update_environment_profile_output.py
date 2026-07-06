"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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


class UpdateEnvironmentProfileOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    """<p>The identifier of the environment profile that is to be udpated.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the environment profile is to be updated.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account in which a specified environment profile is to be udpated.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region in which a specified environment profile is to be updated.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created the environment profile.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment profile was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment profile was updated.</p>"""
    name: "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
    """<p>The name to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>"""
    environment_blueprint_id: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The identifier of the blueprint of the environment profile that is to be updated.</p>"""
    project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project of the environment profile that is to be updated.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentProfileOutput) -> dict:
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


def deserialize_json(data: dict) -> UpdateEnvironmentProfileOutput:
    out: UpdateEnvironmentProfileOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateEnvironmentProfileOutput.id required")
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateEnvironmentProfileOutput.domain_id required")
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsAccountRegion" in data:
        out["aws_account_region"] = data["awsAccountRegion"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("UpdateEnvironmentProfileOutput.created_by required")
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
        raise DeserializationError("UpdateEnvironmentProfileOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "environmentBlueprintId" in data:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentProfileOutput.environment_blueprint_id required"
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
