"""Generated from Smithy shape ``com.amazonaws.inspector2#CisCheckAggregationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_check_aggregation

CisCheckAggregationList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_check_aggregation.CisCheckAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisCheckAggregationList) -> list:
    import aws_sdk_inspector2.types.cis_check_aggregation

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cis_check_aggregation.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisCheckAggregationList:
    import aws_sdk_inspector2.types.cis_check_aggregation

    out: CisCheckAggregationList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_check_aggregation.deserialize_json(item)
        )
    return out
