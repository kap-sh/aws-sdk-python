"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_metadata


class CreateRepositoryOutput(TypedDict, closed=True):
    repository_metadata: NotRequired[
        "aws_sdk_codecommit.types.repository_metadata.RepositoryMetadata"
    ]
    """<p>Information about the newly created repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryOutput) -> dict:
    out: dict = {}
    if "repository_metadata" in value:
        import aws_sdk_codecommit.types.repository_metadata

        out["repositoryMetadata"] = (
            aws_sdk_codecommit.types.repository_metadata.serialize_aws_json_1_1(
                value["repository_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryOutput:
    out: CreateRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "repositoryMetadata" in data:
        import aws_sdk_codecommit.types.repository_metadata

        out["repository_metadata"] = (
            aws_sdk_codecommit.types.repository_metadata.deserialize_aws_json_1_1(
                data["repositoryMetadata"]
            )
        )
    return out
