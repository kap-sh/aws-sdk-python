"""Generated from Smithy shape ``com.amazonaws.codecommit#GetRepositoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_metadata


class GetRepositoryOutput(TypedDict):
    repository_metadata: NotRequired[
        "aws_sdk_codecommit.types.repository_metadata.RepositoryMetadata"
    ]
    """<p>Information about the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRepositoryOutput) -> dict:
    out: dict = {}
    if "repository_metadata" in value:
        import aws_sdk_codecommit.types.repository_metadata

        out["repositoryMetadata"] = (
            aws_sdk_codecommit.types.repository_metadata.serialize_aws_json_1_1(
                value["repository_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRepositoryOutput:
    out: GetRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repositoryMetadata" in data:
        import aws_sdk_codecommit.types.repository_metadata

        out["repository_metadata"] = (
            aws_sdk_codecommit.types.repository_metadata.deserialize_aws_json_1_1(
                data["repositoryMetadata"]
            )
        )
    return out
