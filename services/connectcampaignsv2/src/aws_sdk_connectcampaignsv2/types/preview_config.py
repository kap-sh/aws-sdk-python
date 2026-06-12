"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PreviewConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.agent_actions
    import aws_sdk_connectcampaignsv2.types.bandwidth_allocation
    import aws_sdk_connectcampaignsv2.types.timeout_config


class PreviewConfig(TypedDict):
    bandwidth_allocation: (
        "aws_sdk_connectcampaignsv2.types.bandwidth_allocation.BandwidthAllocation"
    )
    timeout_config: "aws_sdk_connectcampaignsv2.types.timeout_config.TimeoutConfig"
    agent_actions: NotRequired[
        "aws_sdk_connectcampaignsv2.types.agent_actions.AgentActions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PreviewConfig) -> dict:
    out: dict = {}
    out["bandwidthAllocation"] = value["bandwidth_allocation"]
    import aws_sdk_connectcampaignsv2.types.timeout_config

    out["timeoutConfig"] = (
        aws_sdk_connectcampaignsv2.types.timeout_config.serialize_json(
            value["timeout_config"]
        )
    )
    if "agent_actions" in value:
        import aws_sdk_connectcampaignsv2.types.agent_actions

        out["agentActions"] = (
            aws_sdk_connectcampaignsv2.types.agent_actions.serialize_json(
                value["agent_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PreviewConfig:
    out: PreviewConfig = {}  # type: ignore[typeddict-item]
    if "bandwidthAllocation" in data:
        out["bandwidth_allocation"] = data["bandwidthAllocation"]
    else:
        raise DeserializationError("PreviewConfig.bandwidth_allocation required")
    if "timeoutConfig" in data:
        import aws_sdk_connectcampaignsv2.types.timeout_config

        out["timeout_config"] = (
            aws_sdk_connectcampaignsv2.types.timeout_config.deserialize_json(
                data["timeoutConfig"]
            )
        )
    else:
        raise DeserializationError("PreviewConfig.timeout_config required")
    if "agentActions" in data:
        import aws_sdk_connectcampaignsv2.types.agent_actions

        out["agent_actions"] = (
            aws_sdk_connectcampaignsv2.types.agent_actions.deserialize_json(
                data["agentActions"]
            )
        )
    return out
