"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_summary

PredefinedAttributeSummaryList: TypeAlias = list[
    "capo_connect.types.predefined_attribute_summary.PredefinedAttributeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeSummaryList) -> list:
    import capo_connect.types.predefined_attribute_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.predefined_attribute_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PredefinedAttributeSummaryList:
    import capo_connect.types.predefined_attribute_summary

    out: PredefinedAttributeSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.predefined_attribute_summary.deserialize_json(item)
        )
    return out
