"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListCustomPluginsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of_custom_plugin_summary
    import capo_kafkaconnect.types.__string


class ListCustomPluginsResponse(TypedDict, closed=True):
    custom_plugins: NotRequired[
        "capo_kafkaconnect.types.__list_of_custom_plugin_summary.__listOfCustomPluginSummary"
    ]
    """<p>An array of custom plugin descriptions.</p>"""
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response of a ListCustomPlugins operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomPluginsResponse) -> dict:
    out: dict = {}
    if "custom_plugins" in value:
        import capo_kafkaconnect.types.__list_of_custom_plugin_summary

        out["customPlugins"] = (
            capo_kafkaconnect.types.__list_of_custom_plugin_summary.serialize_json(
                value["custom_plugins"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomPluginsResponse:
    out: ListCustomPluginsResponse = {}  # type: ignore[typeddict-item]
    if "customPlugins" in data:
        import capo_kafkaconnect.types.__list_of_custom_plugin_summary

        out["custom_plugins"] = (
            capo_kafkaconnect.types.__list_of_custom_plugin_summary.deserialize_json(
                data["customPlugins"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
