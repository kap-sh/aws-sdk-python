"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetResourceAggregationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_target_resource_aggregation

CisTargetResourceAggregationList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_target_resource_aggregation.CisTargetResourceAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetResourceAggregationList) -> list:
    import aws_sdk_inspector2.types.cis_target_resource_aggregation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_target_resource_aggregation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CisTargetResourceAggregationList:
    import aws_sdk_inspector2.types.cis_target_resource_aggregation

    out: CisTargetResourceAggregationList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_target_resource_aggregation.deserialize_json(
                item
            )
        )
    return out
