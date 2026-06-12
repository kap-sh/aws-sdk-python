"""Generated from Smithy shape ``com.amazonaws.codeartifact#DisassociateExternalConnectionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.repository_description


class DisassociateExternalConnectionResult(TypedDict):
    repository: NotRequired[
        "aws_sdk_codeartifact.types.repository_description.RepositoryDescription"
    ]
    """<p> The repository associated with the removed external connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateExternalConnectionResult) -> dict:
    out: dict = {}
    if "repository" in value:
        import aws_sdk_codeartifact.types.repository_description

        out["repository"] = (
            aws_sdk_codeartifact.types.repository_description.serialize_json(
                value["repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateExternalConnectionResult:
    out: DisassociateExternalConnectionResult = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_codeartifact.types.repository_description

        out["repository"] = (
            aws_sdk_codeartifact.types.repository_description.deserialize_json(
                data["repository"]
            )
        )
    return out
