"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#PluginSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.plugin_summary

PluginSummaries: TypeAlias = list[
    "capo_migrationhuborchestrator.types.plugin_summary.PluginSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginSummaries) -> list:
    import capo_migrationhuborchestrator.types.plugin_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhuborchestrator.types.plugin_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PluginSummaries:
    import capo_migrationhuborchestrator.types.plugin_summary

    out: PluginSummaries = []
    for item in data:
        out.append(
            capo_migrationhuborchestrator.types.plugin_summary.deserialize_json(item)
        )
    return out
