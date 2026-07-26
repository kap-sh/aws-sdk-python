"""Generated from Smithy shape ``com.amazonaws.sagemaker#AgentVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.long


class AgentVersion(TypedDict, closed=True):
    version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>Version of the agent.</p>"""
    agent_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of Edge Manager agents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentVersion) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "agent_count" in value:
        out["AgentCount"] = value["agent_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentVersion:
    out: AgentVersion = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "AgentCount" in data:
        out["agent_count"] = data["AgentCount"]
    return out
