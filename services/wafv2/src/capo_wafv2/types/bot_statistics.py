"""Generated from Smithy shape ``com.amazonaws.wafv2#BotStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.filter_string
    import capo_wafv2.types.percentage_value
    import capo_wafv2.types.request_count


class BotStatistics(TypedDict, closed=True):
    bot_name: "capo_wafv2.types.filter_string.FilterString"
    """<p>The name of the bot. For example, <code>gptbot</code> or <code>googlebot</code>.</p>"""
    request_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The number of requests from this bot to the associated path within the specified time window.</p>"""
    percentage: "capo_wafv2.types.percentage_value.PercentageValue"
    """<p>The percentage of total requests to the associated path that came from this bot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BotStatistics) -> dict:
    out: dict = {}
    out["BotName"] = value["bot_name"]
    out["RequestCount"] = value.get("request_count", 0)
    out["Percentage"] = value.get("percentage", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BotStatistics:
    out: BotStatistics = {}  # type: ignore[typeddict-item]
    if "BotName" in data:
        out["bot_name"] = data["BotName"]
    else:
        raise DeserializationError("BotStatistics.bot_name required")
    if "RequestCount" in data:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    else:
        out["percentage"] = 0
    return out
