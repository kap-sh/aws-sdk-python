"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpstreamRepository``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.repository_name


class UpstreamRepository(TypedDict):
    repository_name: "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of an upstream repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpstreamRepository) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_json(data: dict) -> UpstreamRepository:
    out: UpstreamRepository = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("UpstreamRepository.repository_name required")
    return out
