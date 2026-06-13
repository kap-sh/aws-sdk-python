"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EdgePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.edge_property_summary

EdgePropertyList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.edge_property_summary.EdgePropertySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EdgePropertyList) -> list:
    import aws_sdk_resiliencehubv2.types.edge_property_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.edge_property_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EdgePropertyList:
    import aws_sdk_resiliencehubv2.types.edge_property_summary

    out: EdgePropertyList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.edge_property_summary.deserialize_json(item)
        )
    return out
