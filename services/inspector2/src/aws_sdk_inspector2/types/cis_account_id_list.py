"""Generated from Smithy shape ``com.amazonaws.inspector2#CisAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id

CisAccountIdList: TypeAlias = list["aws_sdk_inspector2.types.account_id.AccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: CisAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CisAccountIdList:
    return list(data)
