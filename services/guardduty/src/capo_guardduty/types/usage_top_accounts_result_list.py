"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageTopAccountsResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.usage_top_accounts_result

UsageTopAccountsResultList: TypeAlias = list[
    "capo_guardduty.types.usage_top_accounts_result.UsageTopAccountsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageTopAccountsResultList) -> list:
    import capo_guardduty.types.usage_top_accounts_result

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.usage_top_accounts_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageTopAccountsResultList:
    import capo_guardduty.types.usage_top_accounts_result

    out: UsageTopAccountsResultList = []
    for item in data:
        out.append(
            capo_guardduty.types.usage_top_accounts_result.deserialize_json(item)
        )
    return out
