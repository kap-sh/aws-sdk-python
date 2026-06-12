"""Generated from Smithy shape ``com.amazonaws.fms#MemberAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id

MemberAccounts: TypeAlias = list["aws_sdk_fms.types.aws_account_id.AWSAccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MemberAccounts:
    return list(data)
