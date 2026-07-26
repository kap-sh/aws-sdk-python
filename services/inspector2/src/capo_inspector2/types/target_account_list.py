"""Generated from Smithy shape ``com.amazonaws.inspector2#TargetAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.target_account

TargetAccountList: TypeAlias = list[
    "capo_inspector2.types.target_account.TargetAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetAccountList) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetAccountList:
    return list(data)
