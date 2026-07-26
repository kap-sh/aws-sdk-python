"""Generated from Smithy shape ``com.amazonaws.codecommit#BranchNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name

BranchNameList: TypeAlias = list["capo_codecommit.types.branch_name.BranchName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BranchNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BranchNameList:
    return list(data)
