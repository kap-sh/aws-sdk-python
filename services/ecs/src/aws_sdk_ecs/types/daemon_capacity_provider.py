"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCapacityProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class DaemonCapacityProvider(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of daemon tasks running on this capacity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonCapacityProvider) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    out["runningCount"] = value.get("running_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonCapacityProvider:
    out: DaemonCapacityProvider = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "runningCount" in data:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    return out
