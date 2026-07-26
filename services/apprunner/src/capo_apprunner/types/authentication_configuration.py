"""Generated from Smithy shape ``com.amazonaws.apprunner#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.role_arn


class AuthenticationConfiguration(TypedDict, closed=True):
    connection_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. It's required for GitHub code repositories.</p>"""
    access_role_arn: NotRequired["capo_apprunner.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "access_role_arn" in value:
        out["AccessRoleArn"] = value["access_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "AccessRoleArn" in data:
        out["access_role_arn"] = data["AccessRoleArn"]
    return out
