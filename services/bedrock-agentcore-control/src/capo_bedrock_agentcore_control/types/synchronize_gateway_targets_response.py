"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SynchronizeGatewayTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_target_list


class SynchronizeGatewayTargetsResponse(TypedDict, closed=True):
    targets: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_target_list.GatewayTargetList"
    ]
    """<p>The gateway targets for synchronization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SynchronizeGatewayTargetsResponse) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_bedrock_agentcore_control.types.gateway_target_list

        out["targets"] = (
            capo_bedrock_agentcore_control.types.gateway_target_list.serialize_json(
                value["targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> SynchronizeGatewayTargetsResponse:
    out: SynchronizeGatewayTargetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_bedrock_agentcore_control.types.gateway_target_list

        out["targets"] = (
            capo_bedrock_agentcore_control.types.gateway_target_list.deserialize_json(
                data["targets"]
            )
        )
    return out
