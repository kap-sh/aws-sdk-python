"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribeRepositoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.repository_description


class DescribeRepositoryResult(TypedDict, closed=True):
    repository: NotRequired[
        "capo_codeartifact.types.repository_description.RepositoryDescription"
    ]
    """<p> A <code>RepositoryDescription</code> object that contains the requested repository information. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRepositoryResult) -> dict:
    out: dict = {}
    if "repository" in value:
        import capo_codeartifact.types.repository_description

        out["repository"] = (
            capo_codeartifact.types.repository_description.serialize_json(
                value["repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeRepositoryResult:
    out: DescribeRepositoryResult = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import capo_codeartifact.types.repository_description

        out["repository"] = (
            capo_codeartifact.types.repository_description.deserialize_json(
                data["repository"]
            )
        )
    return out
