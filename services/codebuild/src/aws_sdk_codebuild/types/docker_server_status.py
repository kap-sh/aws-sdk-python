"""Generated from Smithy shape ``com.amazonaws.codebuild#DockerServerStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string


class DockerServerStatus(TypedDict):
    status: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The status of the docker server.</p>"""
    message: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>A message associated with the status of a docker server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DockerServerStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DockerServerStatus:
    out: DockerServerStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "message" in data:
        out["message"] = data["message"]
    return out
