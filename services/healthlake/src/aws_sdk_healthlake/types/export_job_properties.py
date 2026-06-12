"""Generated from Smithy shape ``com.amazonaws.healthlake#ExportJobProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.iam_role_arn
    import aws_sdk_healthlake.types.job_id
    import aws_sdk_healthlake.types.job_name
    import aws_sdk_healthlake.types.job_status
    import aws_sdk_healthlake.types.message
    import aws_sdk_healthlake.types.output_data_config
    import aws_sdk_healthlake.types.timestamp


class ExportJobProperties(TypedDict):
    job_id: "aws_sdk_healthlake.types.job_id.JobId"
    """<p>The export job identifier.</p>"""
    job_name: NotRequired["aws_sdk_healthlake.types.job_name.JobName"]
    """<p>The export job name.</p>"""
    job_status: "aws_sdk_healthlake.types.job_status.JobStatus"
    """<p>The export job status.</p>"""
    submit_time: "aws_sdk_healthlake.types.timestamp.Timestamp"
    """<p>The time the export job was initiated.</p>"""
    end_time: NotRequired["aws_sdk_healthlake.types.timestamp.Timestamp"]
    """<p>The time the export job completed.</p>"""
    datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier from which files are being exported.</p>"""
    output_data_config: "aws_sdk_healthlake.types.output_data_config.OutputDataConfig"
    """<p>The output data configuration supplied when the export job was created.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_healthlake.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) used during the initiation of the export job.</p>"""
    message: NotRequired["aws_sdk_healthlake.types.message.Message"]
    """<p>An explanation of any errors that might have occurred during the export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportJobProperties) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import aws_sdk_healthlake.types.job_status

    out["JobStatus"] = aws_sdk_healthlake.types.job_status.serialize_aws_json_1_0(
        value["job_status"]
    )
    import aws_sdk_healthlake.types.timestamp

    out["SubmitTime"] = aws_sdk_healthlake.types.timestamp.serialize_aws_json_1_0(
        value["submit_time"]
    )
    if "end_time" in value:
        import aws_sdk_healthlake.types.timestamp

        out["EndTime"] = aws_sdk_healthlake.types.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    out["DatastoreId"] = value["datastore_id"]
    import aws_sdk_healthlake.types.output_data_config

    out["OutputDataConfig"] = (
        aws_sdk_healthlake.types.output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportJobProperties:
    out: ExportJobProperties = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("ExportJobProperties.job_id required")
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_healthlake.types.job_status

        out["job_status"] = (
            aws_sdk_healthlake.types.job_status.deserialize_aws_json_1_0(
                data["JobStatus"]
            )
        )
    else:
        raise DeserializationError("ExportJobProperties.job_status required")
    if "SubmitTime" in data:
        import aws_sdk_healthlake.types.timestamp

        out["submit_time"] = (
            aws_sdk_healthlake.types.timestamp.deserialize_aws_json_1_0(
                data["SubmitTime"]
            )
        )
    else:
        raise DeserializationError("ExportJobProperties.submit_time required")
    if "EndTime" in data:
        import aws_sdk_healthlake.types.timestamp

        out["end_time"] = aws_sdk_healthlake.types.timestamp.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("ExportJobProperties.datastore_id required")
    if "OutputDataConfig" in data:
        import aws_sdk_healthlake.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError("ExportJobProperties.output_data_config required")
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
