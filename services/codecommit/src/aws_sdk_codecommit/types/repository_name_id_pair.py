"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryNameIdPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_id
    import aws_sdk_codecommit.types.repository_name


class RepositoryNameIdPair(TypedDict, closed=True):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name associated with the repository.</p>"""
    repository_id: NotRequired["aws_sdk_codecommit.types.repository_id.RepositoryId"]
    """<p>The ID associated with the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryNameIdPair) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryNameIdPair:
    out: RepositoryNameIdPair = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "repositoryId" in data:
        out["repository_id"] = data["repositoryId"]
    return out
