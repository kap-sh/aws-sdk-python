"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_id


class DeleteRepositoryOutput(TypedDict, closed=True):
    repository_id: NotRequired["capo_codecommit.types.repository_id.RepositoryId"]
    """<p>The ID of the repository that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryOutput) -> dict:
    out: dict = {}
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryOutput:
    out: DeleteRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repositoryId" in data:
        out["repository_id"] = data["repositoryId"]
    return out
