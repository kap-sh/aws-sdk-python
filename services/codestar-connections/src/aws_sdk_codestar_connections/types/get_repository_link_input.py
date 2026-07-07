"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetRepositoryLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.repository_link_id


class GetRepositoryLinkInput(TypedDict, closed=True):
    repository_link_id: (
        "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId"
    )
    """<p>The ID of the repository link to get.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositoryLinkInput) -> dict:
    out: dict = {}
    out["RepositoryLinkId"] = value["repository_link_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositoryLinkInput:
    out: GetRepositoryLinkInput = {}  # type: ignore[typeddict-item]
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        raise DeserializationError("GetRepositoryLinkInput.repository_link_id required")
    return out
