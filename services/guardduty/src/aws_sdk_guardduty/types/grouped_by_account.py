"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_statistics

GroupedByAccount: TypeAlias = list[
    "aws_sdk_guardduty.types.account_statistics.AccountStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByAccount) -> list:
    import aws_sdk_guardduty.types.account_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.account_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByAccount:
    import aws_sdk_guardduty.types.account_statistics

    out: GroupedByAccount = []
    for item in data:
        out.append(aws_sdk_guardduty.types.account_statistics.deserialize_json(item))
    return out
