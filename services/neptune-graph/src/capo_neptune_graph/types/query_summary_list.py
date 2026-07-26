"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QuerySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptune_graph.types.query_summary

QuerySummaryList: TypeAlias = list[
    "capo_neptune_graph.types.query_summary.QuerySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuerySummaryList) -> list:
    import capo_neptune_graph.types.query_summary

    out: list = []
    for item in value:
        out.append(capo_neptune_graph.types.query_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuerySummaryList:
    import capo_neptune_graph.types.query_summary

    out: QuerySummaryList = []
    for item in data:
        out.append(capo_neptune_graph.types.query_summary.deserialize_json(item))
    return out
