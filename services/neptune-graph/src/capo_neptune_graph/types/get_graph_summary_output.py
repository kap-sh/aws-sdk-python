"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphSummaryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptune_graph.types.graph_data_summary


class GetGraphSummaryOutput(TypedDict, closed=True):
    version: NotRequired["str"]
    """<p>Display the version of this tool.</p>"""
    last_statistics_computation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp, in ISO 8601 format, of the time at which Neptune Analytics last computed statistics.</p>"""
    graph_summary: NotRequired[
        "capo_neptune_graph.types.graph_data_summary.GraphDataSummary"
    ]
    """<p>The graph summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphSummaryOutput) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "last_statistics_computation_time" in value:
        import capo_neptune_graph.types._prelude.timestamp

        out["lastStatisticsComputationTime"] = (
            capo_neptune_graph.types._prelude.timestamp.serialize_json(
                value["last_statistics_computation_time"]
            )
        )
    if "graph_summary" in value:
        import capo_neptune_graph.types.graph_data_summary

        out["graphSummary"] = (
            capo_neptune_graph.types.graph_data_summary.serialize_json(
                value["graph_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGraphSummaryOutput:
    out: GetGraphSummaryOutput = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "lastStatisticsComputationTime" in data:
        import capo_neptune_graph.types._prelude.timestamp

        out["last_statistics_computation_time"] = (
            capo_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["lastStatisticsComputationTime"]
            )
        )
    if "graphSummary" in data:
        import capo_neptune_graph.types.graph_data_summary

        out["graph_summary"] = (
            capo_neptune_graph.types.graph_data_summary.deserialize_json(
                data["graphSummary"]
            )
        )
    return out
