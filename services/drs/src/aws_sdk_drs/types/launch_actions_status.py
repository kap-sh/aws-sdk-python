"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.launch_action_runs


class LaunchActionsStatus(TypedDict):
    ssm_agent_discovery_datetime: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Time where the AWS Systems Manager was detected as running on the launched instance.</p>"""
    runs: NotRequired["aws_sdk_drs.types.launch_action_runs.LaunchActionRuns"]
    """<p>List of post launch action status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionsStatus) -> dict:
    out: dict = {}
    if "ssm_agent_discovery_datetime" in value:
        out["ssmAgentDiscoveryDatetime"] = value["ssm_agent_discovery_datetime"]
    if "runs" in value:
        import aws_sdk_drs.types.launch_action_runs

        out["runs"] = aws_sdk_drs.types.launch_action_runs.serialize_json(value["runs"])
    return out


def deserialize_json(data: dict) -> LaunchActionsStatus:
    out: LaunchActionsStatus = {}  # type: ignore[typeddict-item]
    if "ssmAgentDiscoveryDatetime" in data:
        out["ssm_agent_discovery_datetime"] = data["ssmAgentDiscoveryDatetime"]
    if "runs" in data:
        import aws_sdk_drs.types.launch_action_runs

        out["runs"] = aws_sdk_drs.types.launch_action_runs.deserialize_json(
            data["runs"]
        )
    return out
