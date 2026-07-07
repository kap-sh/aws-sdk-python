"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryHeadSourceCodeType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.branch_name


class RepositoryHeadSourceCodeType(TypedDict, closed=True):
    branch_name: "aws_sdk_codeguru_reviewer.types.branch_name.BranchName"
    """<p>The name of the branch in an associated repository. The <code>RepositoryHeadSourceCodeType</code> specifies the tip of this branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryHeadSourceCodeType) -> dict:
    out: dict = {}
    out["BranchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> RepositoryHeadSourceCodeType:
    out: RepositoryHeadSourceCodeType = {}  # type: ignore[typeddict-item]
    if "BranchName" in data:
        out["branch_name"] = data["BranchName"]
    else:
        raise DeserializationError("RepositoryHeadSourceCodeType.branch_name required")
    return out
