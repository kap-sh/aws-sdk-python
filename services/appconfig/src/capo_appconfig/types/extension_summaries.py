"""Generated from Smithy shape ``com.amazonaws.appconfig#ExtensionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.extension_summary

ExtensionSummaries: TypeAlias = list[
    "capo_appconfig.types.extension_summary.ExtensionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionSummaries) -> list:
    import capo_appconfig.types.extension_summary

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.extension_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExtensionSummaries:
    import capo_appconfig.types.extension_summary

    out: ExtensionSummaries = []
    for item in data:
        out.append(capo_appconfig.types.extension_summary.deserialize_json(item))
    return out
