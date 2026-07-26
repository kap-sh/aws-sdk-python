"""Generated from Smithy shape ``com.amazonaws.amplify#GetBranchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.branch_name


class GetBranchRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p>The name of the branch. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBranchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBranchRequest:
    out: GetBranchRequest = {}  # type: ignore[typeddict-item]
    return out
