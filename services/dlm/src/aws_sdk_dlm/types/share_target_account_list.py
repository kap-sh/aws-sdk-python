"""Generated from Smithy shape ``com.amazonaws.dlm#ShareTargetAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.aws_account_id

ShareTargetAccountList: TypeAlias = list[
    "aws_sdk_dlm.types.aws_account_id.AwsAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareTargetAccountList) -> list:
    return list(value)


def deserialize_json(data: list) -> ShareTargetAccountList:
    return list(data)
