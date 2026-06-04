"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_detail


class DescribeDaemonResponse(TypedDict):
    daemon: NotRequired["aws_sdk_ecs.types.daemon_detail.DaemonDetail"]
    """<p>The full description of the daemon, including the current revisions, deployment ARN, cluster, and status information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonResponse) -> dict:
    out: dict = {}
    if "daemon" in value:
        import aws_sdk_ecs.types.daemon_detail

        out["daemon"] = aws_sdk_ecs.types.daemon_detail.serialize_aws_json_1_1(
            value["daemon"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonResponse:
    out: DescribeDaemonResponse = {}  # type: ignore[typeddict-item]
    if "daemon" in data:
        import aws_sdk_ecs.types.daemon_detail

        out["daemon"] = aws_sdk_ecs.types.daemon_detail.deserialize_aws_json_1_1(
            data["daemon"]
        )
    return out
