"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_name
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.timestamp


class AgentStatusReference(TypedDict, closed=True):
    status_start_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The start timestamp of the agent's status.</p>"""
    status_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the agent's status.</p>"""
    status_name: NotRequired["aws_sdk_connect.types.agent_status_name.AgentStatusName"]
    """<p>The name of the agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusReference) -> dict:
    out: dict = {}
    if "status_start_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["StatusStartTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["status_start_timestamp"]
        )
    if "status_arn" in value:
        out["StatusArn"] = value["status_arn"]
    if "status_name" in value:
        out["StatusName"] = value["status_name"]
    return out


def deserialize_json(data: dict) -> AgentStatusReference:
    out: AgentStatusReference = {}  # type: ignore[typeddict-item]
    if "StatusStartTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["status_start_timestamp"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["StatusStartTimestamp"]
            )
        )
    if "StatusArn" in data:
        out["status_arn"] = data["StatusArn"]
    if "StatusName" in data:
        out["status_name"] = data["StatusName"]
    return out
