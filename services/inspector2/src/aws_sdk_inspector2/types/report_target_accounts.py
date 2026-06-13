"""Generated from Smithy shape ``com.amazonaws.inspector2#ReportTargetAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id

ReportTargetAccounts: TypeAlias = list["aws_sdk_inspector2.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: ReportTargetAccounts) -> list:
    return list(value)


def deserialize_json(data: list) -> ReportTargetAccounts:
    return list(data)
