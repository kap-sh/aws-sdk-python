"""Generated from Smithy shape ``com.amazonaws.wafv2#FilterSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.filter_string


class FilterSource(TypedDict, closed=True):
    bot_category: NotRequired["aws_sdk_wafv2.types.filter_string.FilterString"]
    """<p>The bot category that was used to filter the results. For example, <code>ai</code> or <code>search_engine</code>.</p>"""
    bot_organization: NotRequired["aws_sdk_wafv2.types.filter_string.FilterString"]
    """<p>The bot organization that was used to filter the results. For example, <code>OpenAI</code> or <code>Google</code>.</p>"""
    bot_name: NotRequired["aws_sdk_wafv2.types.filter_string.FilterString"]
    """<p>The bot name that was used to filter the results. For example, <code>gptbot</code> or <code>googlebot</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterSource) -> dict:
    out: dict = {}
    if "bot_category" in value:
        out["BotCategory"] = value["bot_category"]
    if "bot_organization" in value:
        out["BotOrganization"] = value["bot_organization"]
    if "bot_name" in value:
        out["BotName"] = value["bot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterSource:
    out: FilterSource = {}  # type: ignore[typeddict-item]
    if "BotCategory" in data:
        out["bot_category"] = data["BotCategory"]
    if "BotOrganization" in data:
        out["bot_organization"] = data["BotOrganization"]
    if "BotName" in data:
        out["bot_name"] = data["BotName"]
    return out
