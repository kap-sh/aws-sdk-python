"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListPluginsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.plugin_summaries


class ListPluginsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    plugins: NotRequired[
        "capo_migrationhuborchestrator.types.plugin_summaries.PluginSummaries"
    ]
    """<p>Migration Hub Orchestrator plugins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "plugins" in value:
        import capo_migrationhuborchestrator.types.plugin_summaries

        out["plugins"] = (
            capo_migrationhuborchestrator.types.plugin_summaries.serialize_json(
                value["plugins"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPluginsResponse:
    out: ListPluginsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "plugins" in data:
        import capo_migrationhuborchestrator.types.plugin_summaries

        out["plugins"] = (
            capo_migrationhuborchestrator.types.plugin_summaries.deserialize_json(
                data["plugins"]
            )
        )
    return out
