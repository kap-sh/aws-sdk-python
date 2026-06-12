"""Generated from Smithy shape ``com.amazonaws.rekognition#GetMediaAnalysisJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.date_time
    import aws_sdk_rekognition.types.kms_key_id
    import aws_sdk_rekognition.types.media_analysis_input
    import aws_sdk_rekognition.types.media_analysis_job_failure_details
    import aws_sdk_rekognition.types.media_analysis_job_id
    import aws_sdk_rekognition.types.media_analysis_job_name
    import aws_sdk_rekognition.types.media_analysis_job_status
    import aws_sdk_rekognition.types.media_analysis_manifest_summary
    import aws_sdk_rekognition.types.media_analysis_operations_config
    import aws_sdk_rekognition.types.media_analysis_output_config
    import aws_sdk_rekognition.types.media_analysis_results


class GetMediaAnalysisJobResponse(TypedDict):
    job_id: "aws_sdk_rekognition.types.media_analysis_job_id.MediaAnalysisJobId"
    """<p>The identifier for the media analysis job.</p>"""
    job_name: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_job_name.MediaAnalysisJobName"
    ]
    """<p>The name of the media analysis job.</p>"""
    operations_config: "aws_sdk_rekognition.types.media_analysis_operations_config.MediaAnalysisOperationsConfig"
    """<p>Operation configurations that were provided during job creation.</p>"""
    status: "aws_sdk_rekognition.types.media_analysis_job_status.MediaAnalysisJobStatus"
    """<p>The current status of the media analysis job.</p>"""
    failure_details: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_job_failure_details.MediaAnalysisJobFailureDetails"
    ]
    """<p>Details about the error that resulted in failure of the job.</p>"""
    creation_timestamp: "aws_sdk_rekognition.types.date_time.DateTime"
    """<p>The Unix date and time when the job was started.</p>"""
    completion_timestamp: NotRequired["aws_sdk_rekognition.types.date_time.DateTime"]
    """<p>The Unix date and time when the job finished.</p>"""
    input: "aws_sdk_rekognition.types.media_analysis_input.MediaAnalysisInput"
    """<p>Reference to the input manifest that was provided in the job creation request.</p>"""
    output_config: "aws_sdk_rekognition.types.media_analysis_output_config.MediaAnalysisOutputConfig"
    """<p>Output configuration that was provided in the creation request.</p>"""
    kms_key_id: NotRequired["aws_sdk_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>KMS Key that was provided in the creation request.</p>"""
    results: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_results.MediaAnalysisResults"
    ]
    """<p>Output manifest that contains prediction results.</p>"""
    manifest_summary: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_manifest_summary.MediaAnalysisManifestSummary"
    ]
    """<p>The summary manifest provides statistics on input manifest and errors identified in the input manifest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMediaAnalysisJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import aws_sdk_rekognition.types.media_analysis_operations_config

    out["OperationsConfig"] = (
        aws_sdk_rekognition.types.media_analysis_operations_config.serialize_aws_json_1_1(
            value["operations_config"]
        )
    )
    import aws_sdk_rekognition.types.media_analysis_job_status

    out["Status"] = (
        aws_sdk_rekognition.types.media_analysis_job_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_details" in value:
        import aws_sdk_rekognition.types.media_analysis_job_failure_details

        out["FailureDetails"] = (
            aws_sdk_rekognition.types.media_analysis_job_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    import aws_sdk_rekognition.types.date_time

    out["CreationTimestamp"] = (
        aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
            value["creation_timestamp"]
        )
    )
    if "completion_timestamp" in value:
        import aws_sdk_rekognition.types.date_time

        out["CompletionTimestamp"] = (
            aws_sdk_rekognition.types.date_time.serialize_aws_json_1_1(
                value["completion_timestamp"]
            )
        )
    import aws_sdk_rekognition.types.media_analysis_input

    out["Input"] = (
        aws_sdk_rekognition.types.media_analysis_input.serialize_aws_json_1_1(
            value["input"]
        )
    )
    import aws_sdk_rekognition.types.media_analysis_output_config

    out["OutputConfig"] = (
        aws_sdk_rekognition.types.media_analysis_output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "results" in value:
        import aws_sdk_rekognition.types.media_analysis_results

        out["Results"] = (
            aws_sdk_rekognition.types.media_analysis_results.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "manifest_summary" in value:
        import aws_sdk_rekognition.types.media_analysis_manifest_summary

        out["ManifestSummary"] = (
            aws_sdk_rekognition.types.media_analysis_manifest_summary.serialize_aws_json_1_1(
                value["manifest_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMediaAnalysisJobResponse:
    out: GetMediaAnalysisJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("GetMediaAnalysisJobResponse.job_id required")
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "OperationsConfig" in data:
        import aws_sdk_rekognition.types.media_analysis_operations_config

        out["operations_config"] = (
            aws_sdk_rekognition.types.media_analysis_operations_config.deserialize_aws_json_1_1(
                data["OperationsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetMediaAnalysisJobResponse.operations_config required"
        )
    if "Status" in data:
        import aws_sdk_rekognition.types.media_analysis_job_status

        out["status"] = (
            aws_sdk_rekognition.types.media_analysis_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("GetMediaAnalysisJobResponse.status required")
    if "FailureDetails" in data:
        import aws_sdk_rekognition.types.media_analysis_job_failure_details

        out["failure_details"] = (
            aws_sdk_rekognition.types.media_analysis_job_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "CreationTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["creation_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetMediaAnalysisJobResponse.creation_timestamp required"
        )
    if "CompletionTimestamp" in data:
        import aws_sdk_rekognition.types.date_time

        out["completion_timestamp"] = (
            aws_sdk_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CompletionTimestamp"]
            )
        )
    if "Input" in data:
        import aws_sdk_rekognition.types.media_analysis_input

        out["input"] = (
            aws_sdk_rekognition.types.media_analysis_input.deserialize_aws_json_1_1(
                data["Input"]
            )
        )
    else:
        raise DeserializationError("GetMediaAnalysisJobResponse.input required")
    if "OutputConfig" in data:
        import aws_sdk_rekognition.types.media_analysis_output_config

        out["output_config"] = (
            aws_sdk_rekognition.types.media_analysis_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError("GetMediaAnalysisJobResponse.output_config required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Results" in data:
        import aws_sdk_rekognition.types.media_analysis_results

        out["results"] = (
            aws_sdk_rekognition.types.media_analysis_results.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "ManifestSummary" in data:
        import aws_sdk_rekognition.types.media_analysis_manifest_summary

        out["manifest_summary"] = (
            aws_sdk_rekognition.types.media_analysis_manifest_summary.deserialize_aws_json_1_1(
                data["ManifestSummary"]
            )
        )
    return out
