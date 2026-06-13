"""Generated from Smithy shape ``com.amazonaws.securityagent#DiscoveredEndpoint``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError


class DiscoveredEndpoint(TypedDict):
    uri: "str"
    """<p>The URI of the discovered endpoint.</p>"""
    pentest_job_id: "str"
    """<p>The unique identifier of the pentest job that discovered the endpoint.</p>"""
    task_id: "str"
    """<p>The unique identifier of the task that discovered the endpoint.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space associated with the discovered endpoint.</p>"""
    evidence: NotRequired["str"]
    """<p>The evidence that led to the discovery of the endpoint.</p>"""
    operation: NotRequired["str"]
    """<p>The HTTP operation associated with the discovered endpoint.</p>"""
    description: NotRequired["str"]
    """<p>A description of the discovered endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredEndpoint) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    out["pentestJobId"] = value["pentest_job_id"]
    out["taskId"] = value["task_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "evidence" in value:
        out["evidence"] = value["evidence"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DiscoveredEndpoint:
    out: DiscoveredEndpoint = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("DiscoveredEndpoint.uri required")
    if "pentestJobId" in data:
        out["pentest_job_id"] = data["pentestJobId"]
    else:
        raise DeserializationError("DiscoveredEndpoint.pentest_job_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("DiscoveredEndpoint.task_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("DiscoveredEndpoint.agent_space_id required")
    if "evidence" in data:
        out["evidence"] = data["evidence"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "description" in data:
        out["description"] = data["description"]
    return out
