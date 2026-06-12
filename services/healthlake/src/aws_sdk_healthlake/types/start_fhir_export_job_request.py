"""Generated from Smithy shape ``com.amazonaws.healthlake#StartFHIRExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.client_token_string
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.iam_role_arn
    import aws_sdk_healthlake.types.job_name
    import aws_sdk_healthlake.types.output_data_config


class StartFHIRExportJobRequest(TypedDict):
    job_name: NotRequired["aws_sdk_healthlake.types.job_name.JobName"]
    """<p>The export job name.</p>"""
    output_data_config: "aws_sdk_healthlake.types.output_data_config.OutputDataConfig"
    """<p>The output data configuration supplied when the export job was started.</p>"""
    datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier from which files are being exported.</p>"""
    data_access_role_arn: "aws_sdk_healthlake.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) used during initiation of the export job.</p>"""
    client_token: NotRequired[
        "aws_sdk_healthlake.types.client_token_string.ClientTokenString"
    ]
    """<p>An optional user provided token used for ensuring API idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFHIRExportJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import aws_sdk_healthlake.types.output_data_config

    out["OutputDataConfig"] = (
        aws_sdk_healthlake.types.output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    out["DatastoreId"] = value["datastore_id"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFHIRExportJobRequest:
    out: StartFHIRExportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "OutputDataConfig" in data:
        import aws_sdk_healthlake.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartFHIRExportJobRequest.output_data_config required"
        )
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("StartFHIRExportJobRequest.datastore_id required")
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartFHIRExportJobRequest.data_access_role_arn required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
