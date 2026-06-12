"""Generated from Smithy shape ``com.amazonaws.m2#CancelBatchJobExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.auth_secrets_manager_arn
    import aws_sdk_m2.types.identifier


class CancelBatchJobExecutionRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""
    execution_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the batch job execution.</p>"""
    auth_secrets_manager_arn: NotRequired[
        "aws_sdk_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
    ]
    """<p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Cancel Batch Job Execution operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelBatchJobExecutionRequest) -> dict:
    out: dict = {}
    if "auth_secrets_manager_arn" in value:
        out["authSecretsManagerArn"] = value["auth_secrets_manager_arn"]
    return out


def deserialize_json(data: dict) -> CancelBatchJobExecutionRequest:
    out: CancelBatchJobExecutionRequest = {}  # type: ignore[typeddict-item]
    if "authSecretsManagerArn" in data:
        out["auth_secrets_manager_arn"] = data["authSecretsManagerArn"]
    return out
