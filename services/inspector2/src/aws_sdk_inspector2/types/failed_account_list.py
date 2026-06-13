"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.failed_account

FailedAccountList: TypeAlias = list[
    "aws_sdk_inspector2.types.failed_account.FailedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedAccountList) -> list:
    import aws_sdk_inspector2.types.failed_account

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.failed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedAccountList:
    import aws_sdk_inspector2.types.failed_account

    out: FailedAccountList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.failed_account.deserialize_json(item))
    return out
