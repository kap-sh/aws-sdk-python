"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetFindingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.finding_id_list


class BatchGetFindingsInput(TypedDict, closed=True):
    finding_ids: "capo_securityagent.types.finding_id_list.FindingIdList"
    """<p>The list of finding identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.finding_id_list

    out["findingIds"] = capo_securityagent.types.finding_id_list.serialize_json(
        value["finding_ids"]
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetFindingsInput:
    out: BatchGetFindingsInput = {}  # type: ignore[typeddict-item]
    if "findingIds" in data:
        import capo_securityagent.types.finding_id_list

        out["finding_ids"] = capo_securityagent.types.finding_id_list.deserialize_json(
            data["findingIds"]
        )
    else:
        raise DeserializationError("BatchGetFindingsInput.finding_ids required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("BatchGetFindingsInput.agent_space_id required")
    return out
