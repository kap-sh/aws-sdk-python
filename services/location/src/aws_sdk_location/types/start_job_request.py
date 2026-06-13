"""Generated from Smithy shape ``com.amazonaws.location#StartJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.client_token
    import aws_sdk_location.types.iam_role_arn
    import aws_sdk_location.types.job_action
    import aws_sdk_location.types.job_action_options
    import aws_sdk_location.types.job_input_options
    import aws_sdk_location.types.job_output_options
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.tag_map


class StartJobRequest(TypedDict):
    client_token: NotRequired["aws_sdk_location.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""
    action: "aws_sdk_location.types.job_action.JobAction"
    """<p>The action to perform on the input data.</p>"""
    action_options: NotRequired[
        "aws_sdk_location.types.job_action_options.JobActionOptions"
    ]
    """<p>Additional parameters that can be requested for each result.</p>"""
    execution_role_arn: "aws_sdk_location.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Location Service assumes during job processing. Amazon Location Service uses this role to access the input and output locations specified for the job.</p> <note> <p>The IAM role must be created in the same Amazon Web Services account where you plan to run your job.</p> </note> <p>For more information about configuring IAM roles for Amazon Location jobs, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html\">Configure IAM permissions</a> in the <i>Amazon Location Service Developer Guide</i>.</p>"""
    input_options: "aws_sdk_location.types.job_input_options.JobInputOptions"
    """<p>Configuration for input data location and format.</p> <note> <p>Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.</p> </note>"""
    name: NotRequired["aws_sdk_location.types.resource_name.ResourceName"]
    """<p>An optional name for the job resource.</p>"""
    output_options: "aws_sdk_location.types.job_output_options.JobOutputOptions"
    """<p>Configuration for output data location and format.</p>"""
    tags: NotRequired["aws_sdk_location.types.tag_map.TagMap"]
    """<p>Tags and corresponding values to be associated with the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Action"] = value["action"]
    if "action_options" in value:
        import aws_sdk_location.types.job_action_options

        out["ActionOptions"] = aws_sdk_location.types.job_action_options.serialize_json(
            value["action_options"]
        )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_location.types.job_input_options

    out["InputOptions"] = aws_sdk_location.types.job_input_options.serialize_json(
        value["input_options"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_location.types.job_output_options

    out["OutputOptions"] = aws_sdk_location.types.job_output_options.serialize_json(
        value["output_options"]
    )
    if "tags" in value:
        import aws_sdk_location.types.tag_map

        out["Tags"] = aws_sdk_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartJobRequest:
    out: StartJobRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Action" in data:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("StartJobRequest.action required")
    if "ActionOptions" in data:
        import aws_sdk_location.types.job_action_options

        out["action_options"] = (
            aws_sdk_location.types.job_action_options.deserialize_json(
                data["ActionOptions"]
            )
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError("StartJobRequest.execution_role_arn required")
    if "InputOptions" in data:
        import aws_sdk_location.types.job_input_options

        out["input_options"] = (
            aws_sdk_location.types.job_input_options.deserialize_json(
                data["InputOptions"]
            )
        )
    else:
        raise DeserializationError("StartJobRequest.input_options required")
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
        raise DeserializationError("StartJobRequest.output_options required")
    if "Tags" in data:
        import aws_sdk_location.types.tag_map

        out["tags"] = aws_sdk_location.types.tag_map.deserialize_json(data["Tags"])
    return out
