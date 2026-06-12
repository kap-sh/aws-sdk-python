"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartJobRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.client_token
    import aws_sdk_emr_serverless.types.configuration_overrides
    import aws_sdk_emr_serverless.types.duration
    import aws_sdk_emr_serverless.types.iam_role_arn
    import aws_sdk_emr_serverless.types.job_driver
    import aws_sdk_emr_serverless.types.job_run_execution_iam_policy
    import aws_sdk_emr_serverless.types.job_run_mode
    import aws_sdk_emr_serverless.types.retry_policy
    import aws_sdk_emr_serverless.types.string256
    import aws_sdk_emr_serverless.types.tag_map


class StartJobRunRequest(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application on which to run the job.</p>"""
    client_token: "aws_sdk_emr_serverless.types.client_token.ClientToken"
    """<p>The client idempotency token of the job run to start. Its value must be unique for each request.</p>"""
    execution_role_arn: "aws_sdk_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The execution role ARN for the job run.</p>"""
    execution_iam_policy: NotRequired[
        "aws_sdk_emr_serverless.types.job_run_execution_iam_policy.JobRunExecutionIamPolicy"
    ]
    """<p>You can pass an optional IAM policy. The resulting job IAM role permissions will be an intersection of this policy and the policy associated with your job execution role.</p>"""
    job_driver: NotRequired["aws_sdk_emr_serverless.types.job_driver.JobDriver"]
    """<p>The job driver for the job run.</p>"""
    configuration_overrides: NotRequired[
        "aws_sdk_emr_serverless.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration overrides for the job run.</p>"""
    tags: NotRequired["aws_sdk_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the job run.</p>"""
    execution_timeout_minutes: NotRequired[
        "aws_sdk_emr_serverless.types.duration.Duration"
    ]
    """<p>The maximum duration for the job run to run. If the job run runs beyond this duration, it will be automatically cancelled.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.string256.String256"]
    """<p>The optional job run name. This doesn't have to be unique.</p>"""
    mode: NotRequired["aws_sdk_emr_serverless.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job run when it starts.</p>"""
    retry_policy: NotRequired["aws_sdk_emr_serverless.types.retry_policy.RetryPolicy"]
    """<p>The retry policy when job run starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "execution_iam_policy" in value:
        import aws_sdk_emr_serverless.types.job_run_execution_iam_policy

        out["executionIamPolicy"] = (
            aws_sdk_emr_serverless.types.job_run_execution_iam_policy.serialize_json(
                value["execution_iam_policy"]
            )
        )
    if "job_driver" in value:
        import aws_sdk_emr_serverless.types.job_driver

        out["jobDriver"] = aws_sdk_emr_serverless.types.job_driver.serialize_json(
            value["job_driver"]
        )
    if "configuration_overrides" in value:
        import aws_sdk_emr_serverless.types.configuration_overrides

        out["configurationOverrides"] = (
            aws_sdk_emr_serverless.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "tags" in value:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "execution_timeout_minutes" in value:
        out["executionTimeoutMinutes"] = value["execution_timeout_minutes"]
    if "name" in value:
        out["name"] = value["name"]
    if "mode" in value:
        out["mode"] = value["mode"]
    if "retry_policy" in value:
        import aws_sdk_emr_serverless.types.retry_policy

        out["retryPolicy"] = aws_sdk_emr_serverless.types.retry_policy.serialize_json(
            value["retry_policy"]
        )
    return out


def deserialize_json(data: dict) -> StartJobRunRequest:
    out: StartJobRunRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("StartJobRunRequest.client_token required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("StartJobRunRequest.execution_role_arn required")
    if "executionIamPolicy" in data:
        import aws_sdk_emr_serverless.types.job_run_execution_iam_policy

        out["execution_iam_policy"] = (
            aws_sdk_emr_serverless.types.job_run_execution_iam_policy.deserialize_json(
                data["executionIamPolicy"]
            )
        )
    if "jobDriver" in data:
        import aws_sdk_emr_serverless.types.job_driver

        out["job_driver"] = aws_sdk_emr_serverless.types.job_driver.deserialize_json(
            data["jobDriver"]
        )
    if "configurationOverrides" in data:
        import aws_sdk_emr_serverless.types.configuration_overrides

        out["configuration_overrides"] = (
            aws_sdk_emr_serverless.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if "tags" in data:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "executionTimeoutMinutes" in data:
        out["execution_timeout_minutes"] = data["executionTimeoutMinutes"]
    if "name" in data:
        out["name"] = data["name"]
    if "mode" in data:
        out["mode"] = data["mode"]
    if "retryPolicy" in data:
        import aws_sdk_emr_serverless.types.retry_policy

        out["retry_policy"] = (
            aws_sdk_emr_serverless.types.retry_policy.deserialize_json(
                data["retryPolicy"]
            )
        )
    return out
