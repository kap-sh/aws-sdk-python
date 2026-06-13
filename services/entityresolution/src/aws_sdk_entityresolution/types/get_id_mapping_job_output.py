"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetIdMappingJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_entityresolution.types.error_details
    import aws_sdk_entityresolution.types.id_mapping_job_metrics
    import aws_sdk_entityresolution.types.id_mapping_job_output_source_config
    import aws_sdk_entityresolution.types.job_id
    import aws_sdk_entityresolution.types.job_status
    import aws_sdk_entityresolution.types.job_type


class GetIdMappingJobOutput(TypedDict):
    job_id: "aws_sdk_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""
    status: "aws_sdk_entityresolution.types.job_status.JobStatus"
    """<p>The current status of the job.</p>"""
    start_time: "datetime.datetime"
    """<p>The time at which the job was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the job has finished.</p>"""
    metrics: NotRequired[
        "aws_sdk_entityresolution.types.id_mapping_job_metrics.IdMappingJobMetrics"
    ]
    """<p>Metrics associated with the execution, specifically total records processed, unique IDs generated, and records the execution skipped.</p>"""
    error_details: NotRequired[
        "aws_sdk_entityresolution.types.error_details.ErrorDetails"
    ]
    output_source_config: NotRequired[
        "aws_sdk_entityresolution.types.id_mapping_job_output_source_config.IdMappingJobOutputSourceConfig"
    ]
    """<p>A list of <code>OutputSource</code> objects.</p>"""
    job_type: NotRequired["aws_sdk_entityresolution.types.job_type.JobType"]
    """<p> The job type of the ID mapping job.</p> <p>A value of <code>INCREMENTAL</code> indicates that only new or changed data was processed since the last job run. This is the default job type if the workflow was created with an <code>incrementalRunConfig</code>.</p> <p>A value of <code>BATCH</code> indicates that all data was processed from the input source, regardless of previous job runs. This is the default job type if the workflow wasn't created with an <code>incrementalRunConfig</code>.</p> <p>A value of <code>DELETE_ONLY</code> indicates that only deletion requests from <code>BatchDeleteUniqueIds</code> were processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingJobOutput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import aws_sdk_entityresolution.types.job_status

    out["status"] = aws_sdk_entityresolution.types.job_status.serialize_json(
        value["status"]
    )
    import aws_sdk_entityresolution.types._prelude.timestamp

    out["startTime"] = aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "metrics" in value:
        import aws_sdk_entityresolution.types.id_mapping_job_metrics

        out["metrics"] = (
            aws_sdk_entityresolution.types.id_mapping_job_metrics.serialize_json(
                value["metrics"]
            )
        )
    if "error_details" in value:
        import aws_sdk_entityresolution.types.error_details

        out["errorDetails"] = (
            aws_sdk_entityresolution.types.error_details.serialize_json(
                value["error_details"]
            )
        )
    if "output_source_config" in value:
        import aws_sdk_entityresolution.types.id_mapping_job_output_source_config

        out["outputSourceConfig"] = (
            aws_sdk_entityresolution.types.id_mapping_job_output_source_config.serialize_json(
                value["output_source_config"]
            )
        )
    if "job_type" in value:
        import aws_sdk_entityresolution.types.job_type

        out["jobType"] = aws_sdk_entityresolution.types.job_type.serialize_json(
            value["job_type"]
        )
    return out


def deserialize_json(data: dict) -> GetIdMappingJobOutput:
    out: GetIdMappingJobOutput = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("GetIdMappingJobOutput.job_id required")
    if "status" in data:
        import aws_sdk_entityresolution.types.job_status

        out["status"] = aws_sdk_entityresolution.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetIdMappingJobOutput.status required")
    if "startTime" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("GetIdMappingJobOutput.start_time required")
    if "endTime" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "metrics" in data:
        import aws_sdk_entityresolution.types.id_mapping_job_metrics

        out["metrics"] = (
            aws_sdk_entityresolution.types.id_mapping_job_metrics.deserialize_json(
                data["metrics"]
            )
        )
    if "errorDetails" in data:
        import aws_sdk_entityresolution.types.error_details

        out["error_details"] = (
            aws_sdk_entityresolution.types.error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if "outputSourceConfig" in data:
        import aws_sdk_entityresolution.types.id_mapping_job_output_source_config

        out["output_source_config"] = (
            aws_sdk_entityresolution.types.id_mapping_job_output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    if "jobType" in data:
        import aws_sdk_entityresolution.types.job_type

        out["job_type"] = aws_sdk_entityresolution.types.job_type.deserialize_json(
            data["jobType"]
        )
    return out
