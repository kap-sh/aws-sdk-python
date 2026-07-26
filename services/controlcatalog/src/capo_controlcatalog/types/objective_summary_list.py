"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.objective_summary

ObjectiveSummaryList: TypeAlias = list[
    "capo_controlcatalog.types.objective_summary.ObjectiveSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveSummaryList) -> list:
    import capo_controlcatalog.types.objective_summary

    out: list = []
    for item in value:
        out.append(capo_controlcatalog.types.objective_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ObjectiveSummaryList:
    import capo_controlcatalog.types.objective_summary

    out: ObjectiveSummaryList = []
    for item in data:
        out.append(capo_controlcatalog.types.objective_summary.deserialize_json(item))
    return out
