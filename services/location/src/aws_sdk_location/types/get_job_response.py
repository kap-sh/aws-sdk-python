"""Generated from Smithy shape ``com.amazonaws.location#GetJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.geo_arn
    import aws_sdk_location.types.iam_role_arn
    import aws_sdk_location.types.job_action
    import aws_sdk_location.types.job_action_options
    import aws_sdk_location.types.job_error
    import aws_sdk_location.types.job_id
    import aws_sdk_location.types.job_input_options
    import aws_sdk_location.types.job_output_options
    import aws_sdk_location.types.job_status
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.tag_map
    import aws_sdk_location.types.timestamp


class GetJobResponse(TypedDict):
    action: "aws_sdk_location.types.job_action.JobAction"
    """<p>Action performed by the job.</p>"""
    action_options: NotRequired[
        "aws_sdk_location.types.job_action_options.JobActionOptions"
    ]
    """<p>Additional options for configuring job action parameters.</p>"""
    created_at: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>Job creation time in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>.</p>"""
    ended_at: NotRequired["aws_sdk_location.types.timestamp.Timestamp"]
    r"""<p>Job completion time in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>. Only returned for jobs in a terminal status: <code>Completed</code> | <code>Failed</code> | <code>Cancelled</code>.</p>"""
    error: NotRequired["aws_sdk_location.types.job_error.JobError"]
    """<p>Error information if the job failed.</p>"""
    execution_role_arn: "aws_sdk_location.types.iam_role_arn.IamRoleArn"
    """<p>IAM role used for permissions when running the job.</p>"""
    input_options: "aws_sdk_location.types.job_input_options.JobInputOptions"
    """<p>Input configuration.</p>"""
    job_arn: "aws_sdk_location.types.geo_arn.GeoArn"
    """<p>Amazon Resource Name (ARN) of the specified job.</p>"""
    job_id: "aws_sdk_location.types.job_id.JobId"
    """<p>Unique job identifier.</p>"""
    name: NotRequired["aws_sdk_location.types.resource_name.ResourceName"]
    """<p>Job name (if provided during creation).</p>"""
    output_options: "aws_sdk_location.types.job_output_options.JobOutputOptions"
    """<p>Output configuration.</p>"""
    status: "aws_sdk_location.types.job_status.JobStatus"
    """<p>Current job status.</p>"""
    updated_at: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>Last update time in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sss</code>.</p>"""
    tags: NotRequired["aws_sdk_location.types.tag_map.TagMap"]
    """<p>Tags and corresponding values associated with the specified job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobResponse) -> dict:
    out: dict = {}
    out["Action"] = value["action"]
    if "action_options" in value:
        import aws_sdk_location.types.job_action_options

        out["ActionOptions"] = aws_sdk_location.types.job_action_options.serialize_json(
            value["action_options"]
        )
    import aws_sdk_location.types.timestamp

    out["CreatedAt"] = aws_sdk_location.types.timestamp.serialize_json(
        value["created_at"]
    )
    if "ended_at" in value:
        import aws_sdk_location.types.timestamp

        out["EndedAt"] = aws_sdk_location.types.timestamp.serialize_json(
            value["ended_at"]
        )
    if "error" in value:
        import aws_sdk_location.types.job_error

        out["Error"] = aws_sdk_location.types.job_error.serialize_json(value["error"])
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_location.types.job_input_options

    out["InputOptions"] = aws_sdk_location.types.job_input_options.serialize_json(
        value["input_options"]
    )
    out["JobArn"] = value["job_arn"]
    out["JobId"] = value["job_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_location.types.job_output_options

    out["OutputOptions"] = aws_sdk_location.types.job_output_options.serialize_json(
        value["output_options"]
    )
    out["Status"] = value["status"]
    import aws_sdk_location.types.timestamp

    out["UpdatedAt"] = aws_sdk_location.types.timestamp.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import aws_sdk_location.types.tag_map

        out["Tags"] = aws_sdk_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetJobResponse:
    out: GetJobResponse = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("GetJobResponse.action required")
    if "ActionOptions" in data:
        import aws_sdk_location.types.job_action_options

        out["action_options"] = (
            aws_sdk_location.types.job_action_options.deserialize_json(
                data["ActionOptions"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_location.types.timestamp

        out["created_at"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("GetJobResponse.created_at required")
    if "EndedAt" in data:
        import aws_sdk_location.types.timestamp

        out["ended_at"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["EndedAt"]
        )
    if "Error" in data:
        import aws_sdk_location.types.job_error

        out["error"] = aws_sdk_location.types.job_error.deserialize_json(data["Error"])
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError("GetJobResponse.execution_role_arn required")
    if "InputOptions" in data:
        import aws_sdk_location.types.job_input_options

        out["input_options"] = (
            aws_sdk_location.types.job_input_options.deserialize_json(
                data["InputOptions"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.input_options required")
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    else:
        raise DeserializationError("GetJobResponse.job_arn required")
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("GetJobResponse.job_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "OutputOptions" in data:
        import aws_sdk_location.types.job_output_options

        out["output_options"] = (
            aws_sdk_location.types.job_output_options.deserialize_json(
                data["OutputOptions"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.output_options required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("GetJobResponse.status required")
    if "UpdatedAt" in data:
        import aws_sdk_location.types.timestamp

        out["updated_at"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("GetJobResponse.updated_at required")
    if "Tags" in data:
        import aws_sdk_location.types.tag_map

        out["tags"] = aws_sdk_location.types.tag_map.deserialize_json(data["Tags"])
    return out
