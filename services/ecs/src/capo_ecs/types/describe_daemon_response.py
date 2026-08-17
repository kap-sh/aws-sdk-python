"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_detail


class DescribeDaemonResponse(TypedDict, closed=True):
    daemon: NotRequired["capo_ecs.types.daemon_detail.DaemonDetail"]
    """<p>The full description of the daemon, including the current revisions, deployment ARN, cluster, and status information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonResponse) -> dict:
    out: dict = {}
    if "daemon" in value:
        import capo_ecs.types.daemon_detail

        out["daemon"] = capo_ecs.types.daemon_detail.serialize_aws_json_1_1(
            value["daemon"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonResponse:
    out: DescribeDaemonResponse = {}  # type: ignore[typeddict-item]
    if data.get("daemon") is not None:
        import capo_ecs.types.daemon_detail

        out["daemon"] = capo_ecs.types.daemon_detail.deserialize_aws_json_1_1(
            data["daemon"]
        )
    return out
