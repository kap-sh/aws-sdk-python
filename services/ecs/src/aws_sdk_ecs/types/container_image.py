"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerImage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ContainerImage(TypedDict):
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    image_digest: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image digest.</p>"""
    image: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container image. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerImage) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "image" in value:
        out["image"] = value["image"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerImage:
    out: ContainerImage = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "image" in data:
        out["image"] = data["image"]
    return out
