"""Generated from Smithy shape ``com.amazonaws.wafv2#BotStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.bot_statistics

BotStatisticsList: TypeAlias = list["capo_wafv2.types.bot_statistics.BotStatistics"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BotStatisticsList) -> list:
    import capo_wafv2.types.bot_statistics

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.bot_statistics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BotStatisticsList:
    import capo_wafv2.types.bot_statistics

    out: BotStatisticsList = []
    for item in data:
        out.append(capo_wafv2.types.bot_statistics.deserialize_aws_json_1_1(item))
    return out
