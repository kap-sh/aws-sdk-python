"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_state

AccountStateList: TypeAlias = list[
    "aws_sdk_inspector2.types.account_state.AccountState"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountStateList) -> list:
    import aws_sdk_inspector2.types.account_state

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.account_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountStateList:
    import aws_sdk_inspector2.types.account_state

    out: AccountStateList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.account_state.deserialize_json(item))
    return out
