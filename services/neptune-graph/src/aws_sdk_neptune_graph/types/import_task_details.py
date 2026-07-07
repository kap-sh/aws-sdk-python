"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ImportTaskDetails(TypedDict, closed=True):
    status: "str"
    """<p>Status of the import task.</p>"""
    start_time: "datetime.datetime"
    """<p>Time at which the import task started.</p>"""
    time_elapsed_seconds: "int"
    """<p>Seconds elapsed since the import task started.</p>"""
    progress_percentage: "int"
    """<p>The percentage progress so far.</p>"""
    error_count: "int"
    """<p>The number of errors encountered so far.</p>"""
    error_details: NotRequired["str"]
    """<p>Details about the errors that have been encountered.</p>"""
    statement_count: "int"
    """<p>The number of statements in the import task.</p>"""
    dictionary_entry_count: "int"
    """<p>The number of dictionary entries in the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskDetails) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import aws_sdk_neptune_graph.types._prelude.timestamp

    out["startTime"] = aws_sdk_neptune_graph.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    out["timeElapsedSeconds"] = value["time_elapsed_seconds"]
    out["progressPercentage"] = value["progress_percentage"]
    out["errorCount"] = value["error_count"]
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    out["statementCount"] = value["statement_count"]
    out["dictionaryEntryCount"] = value["dictionary_entry_count"]
    return out


def deserialize_json(data: dict) -> ImportTaskDetails:
    out: ImportTaskDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportTaskDetails.status required")
    if "startTime" in data:
        import aws_sdk_neptune_graph.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ImportTaskDetails.start_time required")
    if "timeElapsedSeconds" in data:
        out["time_elapsed_seconds"] = data["timeElapsedSeconds"]
    else:
        raise DeserializationError("ImportTaskDetails.time_elapsed_seconds required")
    if "progressPercentage" in data:
        out["progress_percentage"] = data["progressPercentage"]
    else:
        raise DeserializationError("ImportTaskDetails.progress_percentage required")
    if "errorCount" in data:
        out["error_count"] = data["errorCount"]
    else:
        raise DeserializationError("ImportTaskDetails.error_count required")
    if "errorDetails" in data:
        out["error_details"] = data["errorDetails"]
    if "statementCount" in data:
        out["statement_count"] = data["statementCount"]
    else:
        raise DeserializationError("ImportTaskDetails.statement_count required")
    if "dictionaryEntryCount" in data:
        out["dictionary_entry_count"] = data["dictionaryEntryCount"]
    else:
        raise DeserializationError("ImportTaskDetails.dictionary_entry_count required")
    return out
