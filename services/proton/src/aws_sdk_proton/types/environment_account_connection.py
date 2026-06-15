"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentAccountConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.aws_account_id
    import aws_sdk_proton.types.environment_account_connection_arn
    import aws_sdk_proton.types.environment_account_connection_id
    import aws_sdk_proton.types.environment_account_connection_status
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.role_arn


class EnvironmentAccountConnection(TypedDict):
    id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection.</p>"""
    arn: "aws_sdk_proton.types.environment_account_connection_arn.EnvironmentAccountConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the environment account connection.</p>"""
    management_account_id: "aws_sdk_proton.types.aws_account_id.AwsAccountId"
    """<p>The ID of the management account that's connected to the environment account connection.</p>"""
    environment_account_id: "aws_sdk_proton.types.aws_account_id.AwsAccountId"
    """<p>The environment account that's connected to the environment account connection.</p>"""
    role_arn: "aws_sdk_proton.types.arn.Arn"
    """<p>The IAM service role that's associated with the environment account connection.</p>"""
    environment_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment that's associated with the environment account connection.</p>"""
    requested_at: "datetime.datetime"
    """<p>The time when the environment account connection request was made.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the environment account connection was last modified.</p>"""
    status: "aws_sdk_proton.types.environment_account_connection_status.EnvironmentAccountConnectionStatus"
    """<p>The status of the environment account connection.</p>"""
    component_role_arn: NotRequired["aws_sdk_proton.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>"""
    codebuild_role_arn: NotRequired["aws_sdk_proton.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentAccountConnection) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["managementAccountId"] = value["management_account_id"]
    out["environmentAccountId"] = value["environment_account_id"]
    out["roleArn"] = value["role_arn"]
    out["environmentName"] = value["environment_name"]
    import aws_sdk_proton.types._prelude.timestamp

    out["requestedAt"] = aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["requested_at"]
    )
    import aws_sdk_proton.types._prelude.timestamp

    out["lastModifiedAt"] = (
        aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_modified_at"]
        )
    )
    out["status"] = value["status"]
    if "component_role_arn" in value:
        out["componentRoleArn"] = value["component_role_arn"]
    if "codebuild_role_arn" in value:
        out["codebuildRoleArn"] = value["codebuild_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentAccountConnection:
    out: EnvironmentAccountConnection = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("EnvironmentAccountConnection.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnvironmentAccountConnection.arn required")
    if "managementAccountId" in data:
        out["management_account_id"] = data["managementAccountId"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnection.management_account_id required"
        )
    if "environmentAccountId" in data:
        out["environment_account_id"] = data["environmentAccountId"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnection.environment_account_id required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("EnvironmentAccountConnection.role_arn required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError(
            "EnvironmentAccountConnection.environment_name required"
        )
    if "requestedAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["requested_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["requestedAt"]
            )
        )
    else:
        raise DeserializationError("EnvironmentAccountConnection.requested_at required")
    if "lastModifiedAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentAccountConnection.last_modified_at required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("EnvironmentAccountConnection.status required")
    if "componentRoleArn" in data:
        out["component_role_arn"] = data["componentRoleArn"]
    if "codebuildRoleArn" in data:
        out["codebuild_role_arn"] = data["codebuildRoleArn"]
    return out
