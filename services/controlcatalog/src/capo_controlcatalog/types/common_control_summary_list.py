"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_summary

CommonControlSummaryList: TypeAlias = list[
    "capo_controlcatalog.types.common_control_summary.CommonControlSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlSummaryList) -> list:
    import capo_controlcatalog.types.common_control_summary

    out: list = []
    for item in value:
        out.append(
            capo_controlcatalog.types.common_control_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommonControlSummaryList:
    import capo_controlcatalog.types.common_control_summary

    out: CommonControlSummaryList = []
    for item in data:
        out.append(
            capo_controlcatalog.types.common_control_summary.deserialize_json(item)
        )
    return out
