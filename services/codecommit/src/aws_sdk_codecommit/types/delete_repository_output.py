"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteRepositoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_id


class DeleteRepositoryOutput(TypedDict):
    repository_id: NotRequired["aws_sdk_codecommit.types.repository_id.RepositoryId"]
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
