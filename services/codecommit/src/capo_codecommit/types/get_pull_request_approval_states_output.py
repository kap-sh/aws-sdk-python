"""Generated from Smithy shape ``com.amazonaws.codecommit#GetPullRequestApprovalStatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_list


class GetPullRequestApprovalStatesOutput(TypedDict, closed=True):
    approvals: NotRequired["capo_codecommit.types.approval_list.ApprovalList"]
    """<p>Information about users who have approved the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPullRequestApprovalStatesOutput) -> dict:
    out: dict = {}
    if "approvals" in value:
        import capo_codecommit.types.approval_list

        out["approvals"] = capo_codecommit.types.approval_list.serialize_aws_json_1_1(
            value["approvals"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPullRequestApprovalStatesOutput:
    out: GetPullRequestApprovalStatesOutput = {}  # type: ignore[typeddict-item]
    if "approvals" in data:
        import capo_codecommit.types.approval_list

        out["approvals"] = capo_codecommit.types.approval_list.deserialize_aws_json_1_1(
            data["approvals"]
        )
    return out
