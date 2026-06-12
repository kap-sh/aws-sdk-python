"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.user_import_job_name_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class CreateUserImportJobRequest(TypedDict):
    job_name: "aws_sdk_cognito_identity_provider.types.user_import_job_name_type.UserImportJobNameType"
    """<p>A friendly name for the user import job.</p>"""
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to import users into.</p>"""
    cloud_watch_logs_role_arn: (
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    )
    """<p>You must specify an IAM role that has permission to log import-job results to Amazon CloudWatch Logs. This parameter is the ARN of that role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserImportJobRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    out["UserPoolId"] = value["user_pool_id"]
    out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserImportJobRequest:
    out: CreateUserImportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("CreateUserImportJobRequest.job_name required")
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("CreateUserImportJobRequest.user_pool_id required")
    if "CloudWatchLogsRoleArn" in data:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    else:
        raise DeserializationError(
            "CreateUserImportJobRequest.cloud_watch_logs_role_arn required"
        )
    return out
