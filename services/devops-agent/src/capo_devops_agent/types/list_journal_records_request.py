"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListJournalRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.order_type
    import capo_devops_agent.types.resource_id


class ListJournalRecordsRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the execution</p>"""
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the execution whose journal records to retrieve</p>"""
    limit: "int"
    """<p>Maximum number of records to return in a single response (1-100, default: 100)</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results</p>"""
    record_type: "str"
    """<p>Filter records by type (empty string returns all types)</p>"""
    order: "capo_devops_agent.types.order_type.OrderType"
    """<p>Sort order for the records based on timestamp (default: DESC)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJournalRecordsRequest) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    out["limit"] = value.get("limit", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["recordType"] = value.get("record_type", "")
    import capo_devops_agent.types.order_type

    out["order"] = capo_devops_agent.types.order_type.serialize_json(
        value.get("order", "DESC")
    )
    return out


def deserialize_json(data: dict) -> ListJournalRecordsRequest:
    out: ListJournalRecordsRequest = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("ListJournalRecordsRequest.execution_id required")
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recordType" in data:
        out["record_type"] = data["recordType"]
    else:
        out["record_type"] = ""
    if "order" in data:
        import capo_devops_agent.types.order_type

        out["order"] = capo_devops_agent.types.order_type.deserialize_json(
            data["order"]
        )
    else:
        out["order"] = "DESC"
    return out
