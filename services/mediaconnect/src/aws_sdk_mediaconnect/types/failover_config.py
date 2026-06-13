"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.failover_mode
    import aws_sdk_mediaconnect.types.source_priority
    import aws_sdk_mediaconnect.types.state


class FailoverConfig(TypedDict):
    failover_mode: NotRequired["aws_sdk_mediaconnect.types.failover_mode.FailoverMode"]
    """<p> The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.</p>"""
    recovery_window: NotRequired["int"]
    """<p> Search window time to look for dash-7 packets.</p>"""
    source_priority: NotRequired[
        "aws_sdk_mediaconnect.types.source_priority.SourcePriority"
    ]
    """<p> The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.</p>"""
    state: NotRequired["aws_sdk_mediaconnect.types.state.State"]
    """<p>The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverConfig) -> dict:
    out: dict = {}
    if "failover_mode" in value:
        import aws_sdk_mediaconnect.types.failover_mode

        out["failoverMode"] = aws_sdk_mediaconnect.types.failover_mode.serialize_json(
            value["failover_mode"]
        )
    if "recovery_window" in value:
        out["recoveryWindow"] = value["recovery_window"]
    if "source_priority" in value:
        import aws_sdk_mediaconnect.types.source_priority

        out["sourcePriority"] = (
            aws_sdk_mediaconnect.types.source_priority.serialize_json(
                value["source_priority"]
            )
        )
    if "state" in value:
        import aws_sdk_mediaconnect.types.state

        out["state"] = aws_sdk_mediaconnect.types.state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> FailoverConfig:
    out: FailoverConfig = {}  # type: ignore[typeddict-item]
    if "failoverMode" in data:
        import aws_sdk_mediaconnect.types.failover_mode

        out["failover_mode"] = (
            aws_sdk_mediaconnect.types.failover_mode.deserialize_json(
                data["failoverMode"]
            )
        )
    if "recoveryWindow" in data:
        out["recovery_window"] = data["recoveryWindow"]
    if "sourcePriority" in data:
        import aws_sdk_mediaconnect.types.source_priority

        out["source_priority"] = (
            aws_sdk_mediaconnect.types.source_priority.deserialize_json(
                data["sourcePriority"]
            )
        )
    if "state" in data:
        import aws_sdk_mediaconnect.types.state

        out["state"] = aws_sdk_mediaconnect.types.state.deserialize_json(data["state"])
    return out
