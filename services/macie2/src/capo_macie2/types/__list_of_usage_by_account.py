"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUsageByAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.usage_by_account

__listOfUsageByAccount: TypeAlias = list[
    "capo_macie2.types.usage_by_account.UsageByAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUsageByAccount) -> list:
    import capo_macie2.types.usage_by_account

    out: list = []
    for item in value:
        out.append(capo_macie2.types.usage_by_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUsageByAccount:
    import capo_macie2.types.usage_by_account

    out: __listOfUsageByAccount = []
    for item in data:
        out.append(capo_macie2.types.usage_by_account.deserialize_json(item))
    return out
