"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentProfileInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_parameters_list
    import aws_sdk_datazone.types.environment_profile_name
    import aws_sdk_datazone.types.project_id


class CreateEnvironmentProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this environment profile is created.</p>"""
    name: "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
    """<p>The name of this Amazon DataZone environment profile.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone environment profile.</p>"""
    environment_blueprint_identifier: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The ID of the blueprint with which this environment profile is created.</p>"""
    project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project in which to create the environment profile.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters of this Amazon DataZone environment profile.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account in which the Amazon DataZone environment is created.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region in which this environment profile is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentProfileInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentBlueprintIdentifier"] = value["environment_blueprint_identifier"]
    out["projectIdentifier"] = value["project_identifier"]
    if "user_parameters" in value:
        import aws_sdk_datazone.types.environment_parameters_list

        out["userParameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentProfileInput:
    out: CreateEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentProfileInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "environmentBlueprintIdentifier" in data:
        out["environment_blueprint_identifier"] = data["environmentBlueprintIdentifier"]
    else:
        raise DeserializationError(
            "CreateEnvironmentProfileInput.environment_blueprint_identifier required"
        )
    if "projectIdentifier" in data:
        out["project_identifier"] = data["projectIdentifier"]
    else:
        raise DeserializationError(
            "CreateEnvironmentProfileInput.project_identifier required"
        )
    if "userParameters" in data:
        import aws_sdk_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsAccountRegion" in data:
        out["aws_account_region"] = data["awsAccountRegion"]
    return out
