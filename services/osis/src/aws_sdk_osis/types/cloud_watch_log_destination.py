"""Generated from Smithy shape ``com.amazonaws.osis#CloudWatchLogDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.log_group


class CloudWatchLogDestination(TypedDict):
    log_group: "aws_sdk_osis.types.log_group.LogGroup"
    """<p>The name of the CloudWatch Logs group to send pipeline logs to. You can specify an existing log group or create a new one. For example, <code>/aws/vendedlogs/OpenSearchService/pipelines</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogDestination) -> dict:
    out: dict = {}
    out["LogGroup"] = value["log_group"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogDestination:
    out: CloudWatchLogDestination = {}  # type: ignore[typeddict-item]
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    else:
        raise DeserializationError("CloudWatchLogDestination.log_group required")
    return out
