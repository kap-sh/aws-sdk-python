"""Generated from Smithy shape ``com.amazonaws.codecommit#GetRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_metadata


class GetRepositoryOutput(TypedDict, closed=True):
    repository_metadata: NotRequired[
        "capo_codecommit.types.repository_metadata.RepositoryMetadata"
    ]
    """<p>Information about the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRepositoryOutput) -> dict:
    out: dict = {}
    if "repository_metadata" in value:
        import capo_codecommit.types.repository_metadata

        out["repositoryMetadata"] = (
            capo_codecommit.types.repository_metadata.serialize_aws_json_1_1(
                value["repository_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRepositoryOutput:
    out: GetRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repositoryMetadata" in data:
        import capo_codecommit.types.repository_metadata

        out["repository_metadata"] = (
            capo_codecommit.types.repository_metadata.deserialize_aws_json_1_1(
                data["repositoryMetadata"]
            )
        )
    return out
