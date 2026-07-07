"""Generated from Smithy shape ``com.amazonaws.pipes#Pipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.arn
    import aws_sdk_pipes.types.arn_or_url
    import aws_sdk_pipes.types.optional_arn
    import aws_sdk_pipes.types.pipe_arn
    import aws_sdk_pipes.types.pipe_name
    import aws_sdk_pipes.types.pipe_state
    import aws_sdk_pipes.types.pipe_state_reason
    import aws_sdk_pipes.types.requested_pipe_state
    import aws_sdk_pipes.types.timestamp


class Pipe(TypedDict, closed=True):
    name: NotRequired["aws_sdk_pipes.types.pipe_name.PipeName"]
    """<p>The name of the pipe.</p>"""
    arn: NotRequired["aws_sdk_pipes.types.pipe_arn.PipeArn"]
    """<p>The ARN of the pipe.</p>"""
    desired_state: NotRequired[
        "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["aws_sdk_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    state_reason: NotRequired["aws_sdk_pipes.types.pipe_state_reason.PipeStateReason"]
    """<p>The reason the pipe is in its current state.</p>"""
    creation_time: NotRequired["aws_sdk_pipes.types.timestamp.Timestamp"]
    """<p>The time the pipe was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_pipes.types.timestamp.Timestamp"]
    r"""<p>When the pipe was last updated, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    source: NotRequired["aws_sdk_pipes.types.arn_or_url.ArnOrUrl"]
    """<p>The ARN of the source resource.</p>"""
    target: NotRequired["aws_sdk_pipes.types.arn.Arn"]
    """<p>The ARN of the target resource.</p>"""
    enrichment: NotRequired["aws_sdk_pipes.types.optional_arn.OptionalArn"]
    """<p>The ARN of the enrichment resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Pipe) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
    if "current_state" in value:
        out["CurrentState"] = value["current_state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
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
    if "source" in value:
        out["Source"] = value["source"]
    if "target" in value:
        out["Target"] = value["target"]
    if "enrichment" in value:
        out["Enrichment"] = value["enrichment"]
    return out


def deserialize_json(data: dict) -> Pipe:
    out: Pipe = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DesiredState" in data:
        out["desired_state"] = data["DesiredState"]
    if "CurrentState" in data:
        out["current_state"] = data["CurrentState"]
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
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
    if "Source" in data:
        out["source"] = data["Source"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "Enrichment" in data:
        out["enrichment"] = data["Enrichment"]
    return out
