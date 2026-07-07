"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_configuration_id
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.environment_name
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.environment_status
    import aws_sdk_datazone.types.project_id


class EnvironmentSummary(TypedDict, closed=True):
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project in which the environment exists.</p>"""
    id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The identifier of the environment.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the environment exists.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created the environment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment was updated.</p>"""
    name: "aws_sdk_datazone.types.environment_name.EnvironmentName"
    """<p>The name of the environment.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the environment.</p>"""
    environment_profile_id: (
        "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    )
    """<p>The identifier of the environment profile with which the environment was created.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The identifier of the Amazon Web Services account in which an environment exists.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region in which an environment exists.</p>"""
    provider: "str"
    """<p>The provider of the environment.</p>"""
    status: NotRequired["aws_sdk_datazone.types.environment_status.EnvironmentStatus"]
    """<p>The status of the environment.</p>"""
    environment_configuration_id: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_id.EnvironmentConfigurationId"
    ]
    """<p>The configuration ID with which the environment is created.</p>"""
    environment_configuration_name: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name with which the environment is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummary) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    if "id" in value:
        out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
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
    out["environmentProfileId"] = value.get("environment_profile_id", "")
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    out["provider"] = value["provider"]
    if "status" in value:
        import aws_sdk_datazone.types.environment_status

        out["status"] = aws_sdk_datazone.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_configuration_id" in value:
        out["environmentConfigurationId"] = value["environment_configuration_id"]
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> EnvironmentSummary:
    out: EnvironmentSummary = {}  # type: ignore[typeddict-item]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("EnvironmentSummary.project_id required")
    if "id" in data:
        out["id"] = data["id"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("EnvironmentSummary.domain_id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("EnvironmentSummary.created_by required")
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
        raise DeserializationError("EnvironmentSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "environmentProfileId" in data:
        out["environment_profile_id"] = data["environmentProfileId"]
    else:
        out["environment_profile_id"] = ""
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsAccountRegion" in data:
        out["aws_account_region"] = data["awsAccountRegion"]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("EnvironmentSummary.provider required")
    if "status" in data:
        import aws_sdk_datazone.types.environment_status

        out["status"] = aws_sdk_datazone.types.environment_status.deserialize_json(
            data["status"]
        )
    if "environmentConfigurationId" in data:
        out["environment_configuration_id"] = data["environmentConfigurationId"]
    if "environmentConfigurationName" in data:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out
