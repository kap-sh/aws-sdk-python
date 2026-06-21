"""Generated from Smithy shape ``com.amazonaws.fms#AccountRoleStatus``."""

from typing import Literal, TypeAlias, cast

AccountRoleStatus: TypeAlias = Literal[
    "READY",
    "CREATING",
    "PENDING_DELETION",
    "DELETING",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountRoleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountRoleStatus:
    return cast(AccountRoleStatus, data)
