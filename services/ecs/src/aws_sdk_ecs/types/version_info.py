"""Generated from Smithy shape ``com.amazonaws.ecs#VersionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class VersionInfo(TypedDict):
    agent_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The version number of the Amazon ECS container agent.</p>"""
    agent_hash: NotRequired["aws_sdk_ecs.types.string.String"]
    r"""<p>The Git commit hash for the Amazon ECS container agent build on the <a href=\"https://github.com/aws/amazon-ecs-agent\">amazon-ecs-agent </a> GitHub repository.</p>"""
    docker_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Docker version that's running on the container instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionInfo) -> dict:
    out: dict = {}
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    if "agent_hash" in value:
        out["agentHash"] = value["agent_hash"]
    if "docker_version" in value:
        out["dockerVersion"] = value["docker_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VersionInfo:
    out: VersionInfo = {}  # type: ignore[typeddict-item]
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    if "agentHash" in data:
        out["agent_hash"] = data["agentHash"]
    if "dockerVersion" in data:
        out["docker_version"] = data["dockerVersion"]
    return out
