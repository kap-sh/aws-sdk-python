"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeleteRepositoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.repository_description


class DeleteRepositoryResult(TypedDict, closed=True):
    repository: NotRequired[
        "aws_sdk_codeartifact.types.repository_description.RepositoryDescription"
    ]
    """<p> Information about the deleted repository after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRepositoryResult) -> dict:
    out: dict = {}
    if "repository" in value:
        import aws_sdk_codeartifact.types.repository_description

        out["repository"] = (
            aws_sdk_codeartifact.types.repository_description.serialize_json(
                value["repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteRepositoryResult:
    out: DeleteRepositoryResult = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_codeartifact.types.repository_description

        out["repository"] = (
            aws_sdk_codeartifact.types.repository_description.deserialize_json(
                data["repository"]
            )
        )
    return out
