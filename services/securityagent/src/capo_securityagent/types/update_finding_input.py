"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateFindingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.finding_status
    import capo_securityagent.types.risk_level


class UpdateFindingInput(TypedDict, closed=True):
    finding_id: "str"
    """<p>The unique identifier of the finding to update.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the finding.</p>"""
    risk_level: NotRequired["capo_securityagent.types.risk_level.RiskLevel"]
    """<p>The updated risk level for the finding.</p>"""
    status: NotRequired["capo_securityagent.types.finding_status.FindingStatus"]
    """<p>The updated status for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFindingInput) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "risk_level" in value:
        import capo_securityagent.types.risk_level

        out["riskLevel"] = capo_securityagent.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "status" in value:
        import capo_securityagent.types.finding_status

        out["status"] = capo_securityagent.types.finding_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFindingInput:
    out: UpdateFindingInput = {}  # type: ignore[typeddict-item]
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError("UpdateFindingInput.finding_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("UpdateFindingInput.agent_space_id required")
    if "riskLevel" in data:
        import capo_securityagent.types.risk_level

        out["risk_level"] = capo_securityagent.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if "status" in data:
        import capo_securityagent.types.finding_status

        out["status"] = capo_securityagent.types.finding_status.deserialize_json(
            data["status"]
        )
    return out
