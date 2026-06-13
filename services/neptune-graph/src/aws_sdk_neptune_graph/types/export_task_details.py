"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportTaskDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ExportTaskDetails(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start time of the export task.</p>"""
    time_elapsed_seconds: "int"
    """<p>The time elapsed, in seconds, since the start time of the export task.</p>"""
    progress_percentage: "int"
    """<p>The number of progress percentage of the export task.</p>"""
    num_vertices_written: NotRequired["int"]
    """<p>The number of exported vertices.</p>"""
    num_edges_written: NotRequired["int"]
    """<p>The number of exported edges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskDetails) -> dict:
    out: dict = {}
    import aws_sdk_neptune_graph.types._prelude.timestamp

    out["startTime"] = aws_sdk_neptune_graph.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    out["timeElapsedSeconds"] = value["time_elapsed_seconds"]
    out["progressPercentage"] = value["progress_percentage"]
    if "num_vertices_written" in value:
        out["numVerticesWritten"] = value["num_vertices_written"]
    if "num_edges_written" in value:
        out["numEdgesWritten"] = value["num_edges_written"]
    return out


def deserialize_json(data: dict) -> ExportTaskDetails:
    out: ExportTaskDetails = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_neptune_graph.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ExportTaskDetails.start_time required")
    if "timeElapsedSeconds" in data:
        out["time_elapsed_seconds"] = data["timeElapsedSeconds"]
    else:
        raise DeserializationError("ExportTaskDetails.time_elapsed_seconds required")
    if "progressPercentage" in data:
        out["progress_percentage"] = data["progressPercentage"]
    else:
        raise DeserializationError("ExportTaskDetails.progress_percentage required")
    if "numVerticesWritten" in data:
        out["num_vertices_written"] = data["numVerticesWritten"]
    if "numEdgesWritten" in data:
        out["num_edges_written"] = data["numEdgesWritten"]
    return out
