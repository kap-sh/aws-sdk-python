"""Generated from Smithy shape ``com.amazonaws.xray#Edge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.alias_list
    import capo_xray.types.edge_statistics
    import capo_xray.types.histogram
    import capo_xray.types.nullable_integer
    import capo_xray.types.string
    import capo_xray.types.timestamp


class Edge(TypedDict, closed=True):
    reference_id: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>Identifier of the edge. Unique within a service map.</p>"""
    start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The start time of the first segment on the edge.</p>"""
    end_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The end time of the last segment on the edge.</p>"""
    summary_statistics: NotRequired["capo_xray.types.edge_statistics.EdgeStatistics"]
    """<p>Response statistics for segments on the edge.</p>"""
    response_time_histogram: NotRequired["capo_xray.types.histogram.Histogram"]
    """<p>A histogram that maps the spread of client response times on an edge. Only populated for synchronous edges.</p>"""
    aliases: NotRequired["capo_xray.types.alias_list.AliasList"]
    """<p>Aliases for the edge.</p>"""
    edge_type: NotRequired["capo_xray.types.string.String"]
    """<p>Describes an asynchronous connection, with a value of <code>link</code>.</p>"""
    received_event_age_histogram: NotRequired["capo_xray.types.histogram.Histogram"]
    """<p>A histogram that maps the spread of event age when received by consumers. Age is calculated each time an event is received. Only populated when <i>EdgeType</i> is <code>link</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Edge) -> dict:
    out: dict = {}
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "start_time" in value:
        import capo_xray.types.timestamp

        out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_xray.types.timestamp

        out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "summary_statistics" in value:
        import capo_xray.types.edge_statistics

        out["SummaryStatistics"] = capo_xray.types.edge_statistics.serialize_json(
            value["summary_statistics"]
        )
    if "response_time_histogram" in value:
        import capo_xray.types.histogram

        out["ResponseTimeHistogram"] = capo_xray.types.histogram.serialize_json(
            value["response_time_histogram"]
        )
    if "aliases" in value:
        import capo_xray.types.alias_list

        out["Aliases"] = capo_xray.types.alias_list.serialize_json(value["aliases"])
    if "edge_type" in value:
        out["EdgeType"] = value["edge_type"]
    if "received_event_age_histogram" in value:
        import capo_xray.types.histogram

        out["ReceivedEventAgeHistogram"] = capo_xray.types.histogram.serialize_json(
            value["received_event_age_histogram"]
        )
    return out


def deserialize_json(data: dict) -> Edge:
    out: Edge = {}  # type: ignore[typeddict-item]
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    if "StartTime" in data:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    if "SummaryStatistics" in data:
        import capo_xray.types.edge_statistics

        out["summary_statistics"] = capo_xray.types.edge_statistics.deserialize_json(
            data["SummaryStatistics"]
        )
    if "ResponseTimeHistogram" in data:
        import capo_xray.types.histogram

        out["response_time_histogram"] = capo_xray.types.histogram.deserialize_json(
            data["ResponseTimeHistogram"]
        )
    if "Aliases" in data:
        import capo_xray.types.alias_list

        out["aliases"] = capo_xray.types.alias_list.deserialize_json(data["Aliases"])
    if "EdgeType" in data:
        out["edge_type"] = data["EdgeType"]
    if "ReceivedEventAgeHistogram" in data:
        import capo_xray.types.histogram

        out["received_event_age_histogram"] = (
            capo_xray.types.histogram.deserialize_json(
                data["ReceivedEventAgeHistogram"]
            )
        )
    return out
