"""Generated from Smithy shape ``com.amazonaws.codecommit#ListBranchesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name_list
    import aws_sdk_codecommit.types.next_token


class ListBranchesOutput(TypedDict, closed=True):
    branches: NotRequired["aws_sdk_codecommit.types.branch_name_list.BranchNameList"]
    """<p>The list of branch names.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that returns the batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBranchesOutput) -> dict:
    out: dict = {}
    if "branches" in value:
        import aws_sdk_codecommit.types.branch_name_list

        out["branches"] = (
            aws_sdk_codecommit.types.branch_name_list.serialize_aws_json_1_1(
                value["branches"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBranchesOutput:
    out: ListBranchesOutput = {}  # type: ignore[typeddict-item]
    if "branches" in data:
        import aws_sdk_codecommit.types.branch_name_list

        out["branches"] = (
            aws_sdk_codecommit.types.branch_name_list.deserialize_aws_json_1_1(
                data["branches"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
