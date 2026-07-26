"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedAnalysisProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id

AllowedAnalysisProviderList: TypeAlias = list[
    "capo_cleanrooms.types.account_id.AccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAnalysisProviderList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedAnalysisProviderList:
    return list(data)
