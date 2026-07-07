"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.client_token
    import aws_sdk_panorama.types.created_time
    import aws_sdk_panorama.types.job_id
    import aws_sdk_panorama.types.job_tags_list
    import aws_sdk_panorama.types.last_updated_time
    import aws_sdk_panorama.types.package_import_job_input_config
    import aws_sdk_panorama.types.package_import_job_output
    import aws_sdk_panorama.types.package_import_job_output_config
    import aws_sdk_panorama.types.package_import_job_status
    import aws_sdk_panorama.types.package_import_job_status_message
    import aws_sdk_panorama.types.package_import_job_type


class DescribePackageImportJobResponse(TypedDict, closed=True):
    job_id: "aws_sdk_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""
    client_token: NotRequired["aws_sdk_panorama.types.client_token.ClientToken"]
    """<p>The job's client token.</p>"""
    job_type: "aws_sdk_panorama.types.package_import_job_type.PackageImportJobType"
    """<p>The job's type.</p>"""
    input_config: "aws_sdk_panorama.types.package_import_job_input_config.PackageImportJobInputConfig"
    """<p>The job's input config.</p>"""
    output_config: "aws_sdk_panorama.types.package_import_job_output_config.PackageImportJobOutputConfig"
    """<p>The job's output config.</p>"""
    output: "aws_sdk_panorama.types.package_import_job_output.PackageImportJobOutput"
    """<p>The job's output.</p>"""
    created_time: "aws_sdk_panorama.types.created_time.CreatedTime"
    """<p>When the job was created.</p>"""
    last_updated_time: "aws_sdk_panorama.types.last_updated_time.LastUpdatedTime"
    """<p>When the job was updated.</p>"""
    status: "aws_sdk_panorama.types.package_import_job_status.PackageImportJobStatus"
    """<p>The job's status.</p>"""
    status_message: "aws_sdk_panorama.types.package_import_job_status_message.PackageImportJobStatusMessage"
    """<p>The job's status message.</p>"""
    job_tags: NotRequired["aws_sdk_panorama.types.job_tags_list.JobTagsList"]
    """<p>The job's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageImportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["JobType"] = value["job_type"]
    import aws_sdk_panorama.types.package_import_job_input_config

    out["InputConfig"] = (
        aws_sdk_panorama.types.package_import_job_input_config.serialize_json(
            value["input_config"]
        )
    )
    import aws_sdk_panorama.types.package_import_job_output_config

    out["OutputConfig"] = (
        aws_sdk_panorama.types.package_import_job_output_config.serialize_json(
            value["output_config"]
        )
    )
    import aws_sdk_panorama.types.package_import_job_output

    out["Output"] = aws_sdk_panorama.types.package_import_job_output.serialize_json(
        value["output"]
    )
    import aws_sdk_panorama.types.created_time

    out["CreatedTime"] = aws_sdk_panorama.types.created_time.serialize_json(
        value["created_time"]
    )
    import aws_sdk_panorama.types.last_updated_time

    out["LastUpdatedTime"] = aws_sdk_panorama.types.last_updated_time.serialize_json(
        value["last_updated_time"]
    )
    out["Status"] = value["status"]
    out["StatusMessage"] = value["status_message"]
    if "job_tags" in value:
        import aws_sdk_panorama.types.job_tags_list

        out["JobTags"] = aws_sdk_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribePackageImportJobResponse:
    out: DescribePackageImportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribePackageImportJobResponse.job_id required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    else:
        raise DeserializationError("DescribePackageImportJobResponse.job_type required")
    if "InputConfig" in data:
        import aws_sdk_panorama.types.package_import_job_input_config

        out["input_config"] = (
            aws_sdk_panorama.types.package_import_job_input_config.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.input_config required"
        )
    if "OutputConfig" in data:
        import aws_sdk_panorama.types.package_import_job_output_config

        out["output_config"] = (
            aws_sdk_panorama.types.package_import_job_output_config.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.output_config required"
        )
    if "Output" in data:
        import aws_sdk_panorama.types.package_import_job_output

        out["output"] = (
            aws_sdk_panorama.types.package_import_job_output.deserialize_json(
                data["Output"]
            )
        )
    else:
        raise DeserializationError("DescribePackageImportJobResponse.output required")
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.created_time

        out["created_time"] = aws_sdk_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.created_time required"
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_panorama.types.last_updated_time

        out["last_updated_time"] = (
            aws_sdk_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.last_updated_time required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("DescribePackageImportJobResponse.status required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.status_message required"
        )
    if "JobTags" in data:
        import aws_sdk_panorama.types.job_tags_list

        out["job_tags"] = aws_sdk_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out
