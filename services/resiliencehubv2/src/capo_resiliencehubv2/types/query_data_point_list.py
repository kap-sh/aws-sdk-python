"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryDataPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.query_data_point

QueryDataPointList: TypeAlias = list[
    "capo_resiliencehubv2.types.query_data_point.QueryDataPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryDataPointList) -> list:
    import capo_resiliencehubv2.types.query_data_point

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.query_data_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryDataPointList:
    import capo_resiliencehubv2.types.query_data_point

    out: QueryDataPointList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.query_data_point.deserialize_json(item))
    return out
