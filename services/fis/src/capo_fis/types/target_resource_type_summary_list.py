"""Generated from Smithy shape ``com.amazonaws.fis#TargetResourceTypeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.target_resource_type_summary

TargetResourceTypeSummaryList: TypeAlias = list[
    "capo_fis.types.target_resource_type_summary.TargetResourceTypeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetResourceTypeSummaryList) -> list:
    import capo_fis.types.target_resource_type_summary

    out: list = []
    for item in value:
        out.append(capo_fis.types.target_resource_type_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetResourceTypeSummaryList:
    import capo_fis.types.target_resource_type_summary

    out: TargetResourceTypeSummaryList = []
    for item in data:
        out.append(capo_fis.types.target_resource_type_summary.deserialize_json(item))
    return out
