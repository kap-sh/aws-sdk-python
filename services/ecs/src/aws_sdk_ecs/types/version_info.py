"""Generated from Smithy shape ``com.amazonaws.ecs#VersionInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class VersionInfo(TypedDict):
    agent_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The version number of the Amazon ECS container agent.</p>"""
    agent_hash: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Git commit hash for the Amazon ECS container agent build on the <a href=\"https://github.com/aws/amazon-ecs-agent\">amazon-ecs-agent </a> GitHub repository.</p>"""
    docker_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Docker version that's running on the container instance.</p>"""
