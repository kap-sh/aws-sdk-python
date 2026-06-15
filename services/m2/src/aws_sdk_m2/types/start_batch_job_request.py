"""Generated from Smithy shape ``com.amazonaws.m2#StartBatchJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.auth_secrets_manager_arn
    import aws_sdk_m2.types.batch_job_identifier
    import aws_sdk_m2.types.batch_job_parameters_map
    import aws_sdk_m2.types.identifier


class StartBatchJobRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application associated with this batch job.</p>"""
    batch_job_identifier: "aws_sdk_m2.types.batch_job_identifier.BatchJobIdentifier"
    """<p>The unique identifier of the batch job.</p>"""
    job_params: NotRequired[
        "aws_sdk_m2.types.batch_job_parameters_map.BatchJobParametersMap"
    ]
    r"""<p>The collection of batch job parameters. For details about limits for keys and values, see <a href=\"https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl\">Coding variables in JCL</a>.</p>"""
    auth_secrets_manager_arn: NotRequired[
        "aws_sdk_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
    ]
    """<p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Start Batch Job execution operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBatchJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.batch_job_identifier

    out["batchJobIdentifier"] = aws_sdk_m2.types.batch_job_identifier.serialize_json(
        value["batch_job_identifier"]
    )
    if "job_params" in value:
        import aws_sdk_m2.types.batch_job_parameters_map

        out["jobParams"] = aws_sdk_m2.types.batch_job_parameters_map.serialize_json(
            value["job_params"]
        )
    if "auth_secrets_manager_arn" in value:
        out["authSecretsManagerArn"] = value["auth_secrets_manager_arn"]
    return out


def deserialize_json(data: dict) -> StartBatchJobRequest:
    out: StartBatchJobRequest = {}  # type: ignore[typeddict-item]
    if "batchJobIdentifier" in data:
        import aws_sdk_m2.types.batch_job_identifier

        out["batch_job_identifier"] = (
            aws_sdk_m2.types.batch_job_identifier.deserialize_json(
                data["batchJobIdentifier"]
            )
        )
    else:
        raise DeserializationError("StartBatchJobRequest.batch_job_identifier required")
    if "jobParams" in data:
        import aws_sdk_m2.types.batch_job_parameters_map

        out["job_params"] = aws_sdk_m2.types.batch_job_parameters_map.deserialize_json(
            data["jobParams"]
        )
    if "authSecretsManagerArn" in data:
        out["auth_secrets_manager_arn"] = data["authSecretsManagerArn"]
    return out
