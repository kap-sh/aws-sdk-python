"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EdgePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.edge_property_summary

EdgePropertyList: TypeAlias = list[
    "capo_resiliencehubv2.types.edge_property_summary.EdgePropertySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EdgePropertyList) -> list:
    import capo_resiliencehubv2.types.edge_property_summary

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.edge_property_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EdgePropertyList:
    import capo_resiliencehubv2.types.edge_property_summary

    out: EdgePropertyList = []
    for item in data:
        out.append(
            capo_resiliencehubv2.types.edge_property_summary.deserialize_json(item)
        )
    return out
