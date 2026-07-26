"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.account_statistics

GroupedByAccount: TypeAlias = list[
    "capo_guardduty.types.account_statistics.AccountStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByAccount) -> list:
    import capo_guardduty.types.account_statistics

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.account_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByAccount:
    import capo_guardduty.types.account_statistics

    out: GroupedByAccount = []
    for item in data:
        out.append(capo_guardduty.types.account_statistics.deserialize_json(item))
    return out
