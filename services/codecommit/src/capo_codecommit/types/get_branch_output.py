"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBranchOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_info


class GetBranchOutput(TypedDict, closed=True):
    branch: NotRequired["capo_codecommit.types.branch_info.BranchInfo"]
    """<p>The name of the branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBranchOutput) -> dict:
    out: dict = {}
    if "branch" in value:
        import capo_codecommit.types.branch_info

        out["branch"] = capo_codecommit.types.branch_info.serialize_aws_json_1_1(
            value["branch"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBranchOutput:
    out: GetBranchOutput = {}  # type: ignore[typeddict-item]
    if "branch" in data:
        import capo_codecommit.types.branch_info

        out["branch"] = capo_codecommit.types.branch_info.deserialize_aws_json_1_1(
            data["branch"]
        )
    return out
