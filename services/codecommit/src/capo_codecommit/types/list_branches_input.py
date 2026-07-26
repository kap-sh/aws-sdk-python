"""Generated from Smithy shape ``com.amazonaws.codecommit#ListBranchesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.next_token
    import capo_codecommit.types.repository_name


class ListBranchesInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the branches.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBranchesInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBranchesInput:
    out: ListBranchesInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("ListBranchesInput.repository_name required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
