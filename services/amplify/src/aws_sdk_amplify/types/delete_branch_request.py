"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteBranchRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.branch_name


class DeleteBranchRequest(TypedDict):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    branch_name: "aws_sdk_amplify.types.branch_name.BranchName"
    """<p>The name of the branch. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBranchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBranchRequest:
    out: DeleteBranchRequest = {}  # type: ignore[typeddict-item]
    return out
