"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StatisticalIssueStatus``."""

from typing import Literal, TypeAlias, cast

StatisticalIssueStatus: TypeAlias = Literal[
    "POTENTIAL_ISSUE_DETECTED",
    "NO_ISSUE_DETECTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatisticalIssueStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatisticalIssueStatus:
    return cast(StatisticalIssueStatus, data)
