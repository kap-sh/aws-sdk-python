"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageTopAccountsByFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.usage_top_account_result

UsageTopAccountsByFeatureList: TypeAlias = list[
    "capo_guardduty.types.usage_top_account_result.UsageTopAccountResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageTopAccountsByFeatureList) -> list:
    import capo_guardduty.types.usage_top_account_result

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.usage_top_account_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageTopAccountsByFeatureList:
    import capo_guardduty.types.usage_top_account_result

    out: UsageTopAccountsByFeatureList = []
    for item in data:
        out.append(capo_guardduty.types.usage_top_account_result.deserialize_json(item))
    return out
