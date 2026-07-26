"""Generated from Smithy shape ``com.amazonaws.healthlake#ImportJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.iam_role_arn
    import capo_healthlake.types.input_data_config
    import capo_healthlake.types.job_id
    import capo_healthlake.types.job_name
    import capo_healthlake.types.job_progress_report
    import capo_healthlake.types.job_status
    import capo_healthlake.types.message
    import capo_healthlake.types.output_data_config
    import capo_healthlake.types.timestamp
    import capo_healthlake.types.validation_level


class ImportJobProperties(TypedDict, closed=True):
    job_id: "capo_healthlake.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_name: NotRequired["capo_healthlake.types.job_name.JobName"]
    """<p>The import job name.</p>"""
    job_status: "capo_healthlake.types.job_status.JobStatus"
    """<p>The import job status.</p>"""
    submit_time: "capo_healthlake.types.timestamp.Timestamp"
    """<p>The time the import job was submitted for processing.</p>"""
    end_time: NotRequired["capo_healthlake.types.timestamp.Timestamp"]
    """<p>The time the import job was completed.</p>"""
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier. </p>"""
    input_data_config: "capo_healthlake.types.input_data_config.InputDataConfig"
    """<p>The input data configuration supplied when the import job was created.</p>"""
    job_output_data_config: NotRequired[
        "capo_healthlake.types.output_data_config.OutputDataConfig"
    ]
    job_progress_report: NotRequired[
        "capo_healthlake.types.job_progress_report.JobProgressReport"
    ]
    """<p>Displays the progress of the import job, including total resources scanned, total resources imported, and total size of data imported.</p>"""
    data_access_role_arn: NotRequired["capo_healthlake.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) that grants AWS HealthLake access to the input data.</p>"""
    message: NotRequired["capo_healthlake.types.message.Message"]
    """<p>An explanation of any errors that might have occurred during the FHIR import job.</p>"""
    validation_level: NotRequired[
        "capo_healthlake.types.validation_level.ValidationLevel"
    ]
    """<p>The validation level of the import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJobProperties) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_healthlake.types.job_status

    out["JobStatus"] = capo_healthlake.types.job_status.serialize_aws_json_1_0(
        value["job_status"]
    )
    import capo_healthlake.types.timestamp

    out["SubmitTime"] = capo_healthlake.types.timestamp.serialize_aws_json_1_0(
        value["submit_time"]
    )
    if "end_time" in value:
        import capo_healthlake.types.timestamp

        out["EndTime"] = capo_healthlake.types.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    out["DatastoreId"] = value["datastore_id"]
    import capo_healthlake.types.input_data_config

    out["InputDataConfig"] = (
        capo_healthlake.types.input_data_config.serialize_aws_json_1_0(
            value["input_data_config"]
        )
    )
    if "job_output_data_config" in value:
        import capo_healthlake.types.output_data_config

        out["JobOutputDataConfig"] = (
            capo_healthlake.types.output_data_config.serialize_aws_json_1_0(
                value["job_output_data_config"]
            )
        )
    if "job_progress_report" in value:
        import capo_healthlake.types.job_progress_report

        out["JobProgressReport"] = (
            capo_healthlake.types.job_progress_report.serialize_aws_json_1_0(
                value["job_progress_report"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    if "validation_level" in value:
        import capo_healthlake.types.validation_level

        out["ValidationLevel"] = (
            capo_healthlake.types.validation_level.serialize_aws_json_1_0(
                value["validation_level"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportJobProperties:
    out: ImportJobProperties = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("ImportJobProperties.job_id required")
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import capo_healthlake.types.job_status

        out["job_status"] = capo_healthlake.types.job_status.deserialize_aws_json_1_0(
            data["JobStatus"]
        )
    else:
        raise DeserializationError("ImportJobProperties.job_status required")
    if "SubmitTime" in data:
        import capo_healthlake.types.timestamp

        out["submit_time"] = capo_healthlake.types.timestamp.deserialize_aws_json_1_0(
            data["SubmitTime"]
        )
    else:
        raise DeserializationError("ImportJobProperties.submit_time required")
    if "EndTime" in data:
        import capo_healthlake.types.timestamp

        out["end_time"] = capo_healthlake.types.timestamp.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("ImportJobProperties.datastore_id required")
    if "InputDataConfig" in data:
        import capo_healthlake.types.input_data_config

        out["input_data_config"] = (
            capo_healthlake.types.input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError("ImportJobProperties.input_data_config required")
    if "JobOutputDataConfig" in data:
        import capo_healthlake.types.output_data_config

        out["job_output_data_config"] = (
            capo_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["JobOutputDataConfig"]
            )
        )
    if "JobProgressReport" in data:
        import capo_healthlake.types.job_progress_report

        out["job_progress_report"] = (
            capo_healthlake.types.job_progress_report.deserialize_aws_json_1_0(
                data["JobProgressReport"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ValidationLevel" in data:
        import capo_healthlake.types.validation_level

        out["validation_level"] = (
            capo_healthlake.types.validation_level.deserialize_aws_json_1_0(
                data["ValidationLevel"]
            )
        )
    return out
