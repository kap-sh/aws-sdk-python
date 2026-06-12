"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CodeCommitRepository``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.name


class CodeCommitRepository(TypedDict):
    name: "aws_sdk_codeguru_reviewer.types.name.Name"
    """<p>The name of the Amazon Web Services CodeCommit repository. For more information, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetRepository.html#CodeCommit-GetRepository-request-repositoryName\">repositoryName</a> in the <i>Amazon Web Services CodeCommit API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeCommitRepository) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CodeCommitRepository:
    out: CodeCommitRepository = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CodeCommitRepository.name required")
    return out
