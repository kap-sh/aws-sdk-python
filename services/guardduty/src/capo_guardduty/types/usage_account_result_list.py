"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageAccountResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.usage_account_result

UsageAccountResultList: TypeAlias = list[
    "capo_guardduty.types.usage_account_result.UsageAccountResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageAccountResultList) -> list:
    import capo_guardduty.types.usage_account_result

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.usage_account_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageAccountResultList:
    import capo_guardduty.types.usage_account_result

    out: UsageAccountResultList = []
    for item in data:
        out.append(capo_guardduty.types.usage_account_result.deserialize_json(item))
    return out
