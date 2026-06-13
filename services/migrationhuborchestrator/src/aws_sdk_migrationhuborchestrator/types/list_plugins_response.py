"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListPluginsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.plugin_summaries


class ListPluginsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    plugins: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.plugin_summaries.PluginSummaries"
    ]
    """<p>Migration Hub Orchestrator plugins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "plugins" in value:
        import aws_sdk_migrationhuborchestrator.types.plugin_summaries

        out["plugins"] = (
            aws_sdk_migrationhuborchestrator.types.plugin_summaries.serialize_json(
                value["plugins"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPluginsResponse:
    out: ListPluginsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "plugins" in data:
        import aws_sdk_migrationhuborchestrator.types.plugin_summaries

        out["plugins"] = (
            aws_sdk_migrationhuborchestrator.types.plugin_summaries.deserialize_json(
                data["plugins"]
            )
        )
    return out
