"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#BranchDiffSourceCodeType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.branch_name


class BranchDiffSourceCodeType(TypedDict, closed=True):
    source_branch_name: "aws_sdk_codeguru_reviewer.types.branch_name.BranchName"
    """<p>The source branch for a diff in an associated repository.</p>"""
    destination_branch_name: "aws_sdk_codeguru_reviewer.types.branch_name.BranchName"
    """<p>The destination branch for a diff in an associated repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BranchDiffSourceCodeType) -> dict:
    out: dict = {}
    out["SourceBranchName"] = value["source_branch_name"]
    out["DestinationBranchName"] = value["destination_branch_name"]
    return out


def deserialize_json(data: dict) -> BranchDiffSourceCodeType:
    out: BranchDiffSourceCodeType = {}  # type: ignore[typeddict-item]
    if "SourceBranchName" in data:
        out["source_branch_name"] = data["SourceBranchName"]
    else:
        raise DeserializationError(
            "BranchDiffSourceCodeType.source_branch_name required"
        )
    if "DestinationBranchName" in data:
        out["destination_branch_name"] = data["DestinationBranchName"]
    else:
        raise DeserializationError(
            "BranchDiffSourceCodeType.destination_branch_name required"
        )
    return out
