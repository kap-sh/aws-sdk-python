"""Generated from Smithy shape ``com.amazonaws.pipes#UpdatePipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.pipe_arn
    import aws_sdk_pipes.types.pipe_name
    import aws_sdk_pipes.types.pipe_state
    import aws_sdk_pipes.types.requested_pipe_state
    import aws_sdk_pipes.types.timestamp


class UpdatePipeResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pipes.types.pipe_arn.PipeArn"]
    """<p>The ARN of the pipe.</p>"""
    name: NotRequired["aws_sdk_pipes.types.pipe_name.PipeName"]
    """<p>The name of the pipe.</p>"""
    desired_state: NotRequired[
        "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["aws_sdk_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    creation_time: NotRequired["aws_sdk_pipes.types.timestamp.Timestamp"]
    """<p>The time the pipe was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_pipes.types.timestamp.Timestamp"]
    r"""<p>When the pipe was last updated, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipeResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
    if "current_state" in value:
        out["CurrentState"] = value["current_state"]
    if "creation_time" in value:
        import aws_sdk_pipes.types.timestamp

        out["CreationTime"] = aws_sdk_pipes.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_pipes.types.timestamp

        out["LastModifiedTime"] = aws_sdk_pipes.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePipeResponse:
    out: UpdatePipeResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DesiredState" in data:
        out["desired_state"] = data["DesiredState"]
    if "CurrentState" in data:
        out["current_state"] = data["CurrentState"]
    if "CreationTime" in data:
        import aws_sdk_pipes.types.timestamp

        out["creation_time"] = aws_sdk_pipes.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_pipes.types.timestamp

        out["last_modified_time"] = aws_sdk_pipes.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
