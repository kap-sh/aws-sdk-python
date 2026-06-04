"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteDaemonRequest(TypedDict):
    daemon_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDaemonRequest) -> dict:
    out: dict = {}
    out["daemonArn"] = value["daemon_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDaemonRequest:
    out: DeleteDaemonRequest = {}  # type: ignore[typeddict-item]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    else:
        raise DeserializationError("DeleteDaemonRequest.daemon_arn required")
    return out
