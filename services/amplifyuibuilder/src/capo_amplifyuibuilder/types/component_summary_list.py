"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_summary

ComponentSummaryList: TypeAlias = list[
    "capo_amplifyuibuilder.types.component_summary.ComponentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummaryList) -> list:
    import capo_amplifyuibuilder.types.component_summary

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.component_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentSummaryList:
    import capo_amplifyuibuilder.types.component_summary

    out: ComponentSummaryList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.component_summary.deserialize_json(item))
    return out
