"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalState``."""

from typing import Literal, TypeAlias, cast

ApprovalState: TypeAlias = Literal[
    "APPROVE",
    "REVOKE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApprovalState:
    return cast(ApprovalState, data)
