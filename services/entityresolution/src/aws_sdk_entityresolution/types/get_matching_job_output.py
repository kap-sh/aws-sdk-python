"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchingJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_entityresolution.types.error_details
    import aws_sdk_entityresolution.types.job_id
    import aws_sdk_entityresolution.types.job_metrics
    import aws_sdk_entityresolution.types.job_output_source_config
    import aws_sdk_entityresolution.types.job_status


class GetMatchingJobOutput(TypedDict):
    job_id: "aws_sdk_entityresolution.types.job_id.JobId"
    """<p>The unique identifier of the matching job.</p>"""
    status: "aws_sdk_entityresolution.types.job_status.JobStatus"
    """<p>The current status of the job.</p>"""
    start_time: "datetime.datetime"
    """<p>The time at which the job was started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the job has finished.</p>"""
    metrics: NotRequired["aws_sdk_entityresolution.types.job_metrics.JobMetrics"]
    """<p>Metrics associated with the execution, specifically total records processed, unique IDs generated, and records the execution skipped.</p>"""
    error_details: NotRequired[
        "aws_sdk_entityresolution.types.error_details.ErrorDetails"
    ]
    """<p>An object containing an error message, if there was an error.</p>"""
    output_source_config: NotRequired[
        "aws_sdk_entityresolution.types.job_output_source_config.JobOutputSourceConfig"
    ]
    """<p>A list of <code>OutputSource</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchingJobOutput) -> dict:
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
        import aws_sdk_entityresolution.types.job_metrics

        out["metrics"] = aws_sdk_entityresolution.types.job_metrics.serialize_json(
            value["metrics"]
        )
    if "error_details" in value:
        import aws_sdk_entityresolution.types.error_details

        out["errorDetails"] = (
            aws_sdk_entityresolution.types.error_details.serialize_json(
                value["error_details"]
            )
        )
    if "output_source_config" in value:
        import aws_sdk_entityresolution.types.job_output_source_config

        out["outputSourceConfig"] = (
            aws_sdk_entityresolution.types.job_output_source_config.serialize_json(
                value["output_source_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMatchingJobOutput:
    out: GetMatchingJobOutput = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("GetMatchingJobOutput.job_id required")
    if "status" in data:
        import aws_sdk_entityresolution.types.job_status

        out["status"] = aws_sdk_entityresolution.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetMatchingJobOutput.status required")
    if "startTime" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("GetMatchingJobOutput.start_time required")
    if "endTime" in data:
        import aws_sdk_entityresolution.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_entityresolution.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "metrics" in data:
        import aws_sdk_entityresolution.types.job_metrics

        out["metrics"] = aws_sdk_entityresolution.types.job_metrics.deserialize_json(
            data["metrics"]
        )
    if "errorDetails" in data:
        import aws_sdk_entityresolution.types.error_details

        out["error_details"] = (
            aws_sdk_entityresolution.types.error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if "outputSourceConfig" in data:
        import aws_sdk_entityresolution.types.job_output_source_config

        out["output_source_config"] = (
            aws_sdk_entityresolution.types.job_output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    return out
