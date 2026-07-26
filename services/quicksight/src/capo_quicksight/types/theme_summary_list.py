"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.theme_summary

ThemeSummaryList: TypeAlias = list["capo_quicksight.types.theme_summary.ThemeSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeSummaryList) -> list:
    import capo_quicksight.types.theme_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.theme_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeSummaryList:
    import capo_quicksight.types.theme_summary

    out: ThemeSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.theme_summary.deserialize_json(item))
    return out
