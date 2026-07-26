"""Generated from Smithy shape ``com.amazonaws.configservice#MemberAccountRuleStatus``."""

from typing import Literal, TypeAlias, cast

MemberAccountRuleStatus: TypeAlias = Literal[
    "CREATE_SUCCESSFUL",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberAccountRuleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MemberAccountRuleStatus:
    return cast(MemberAccountRuleStatus, data)
