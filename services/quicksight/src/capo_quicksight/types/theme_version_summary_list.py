"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.theme_version_summary

ThemeVersionSummaryList: TypeAlias = list[
    "capo_quicksight.types.theme_version_summary.ThemeVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeVersionSummaryList) -> list:
    import capo_quicksight.types.theme_version_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.theme_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeVersionSummaryList:
    import capo_quicksight.types.theme_version_summary

    out: ThemeVersionSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.theme_version_summary.deserialize_json(item))
    return out
