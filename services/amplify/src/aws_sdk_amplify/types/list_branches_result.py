"""Generated from Smithy shape ``com.amazonaws.amplify#ListBranchesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.branches
    import aws_sdk_amplify.types.next_token


class ListBranchesResult(TypedDict, closed=True):
    branches: "aws_sdk_amplify.types.branches.Branches"
    """<p> A list of branches for an Amplify app. </p>"""
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p> A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBranchesResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.branches

    out["branches"] = aws_sdk_amplify.types.branches.serialize_json(value["branches"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBranchesResult:
    out: ListBranchesResult = {}  # type: ignore[typeddict-item]
    if "branches" in data:
        import aws_sdk_amplify.types.branches

        out["branches"] = aws_sdk_amplify.types.branches.deserialize_json(
            data["branches"]
        )
    else:
        raise DeserializationError("ListBranchesResult.branches required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
