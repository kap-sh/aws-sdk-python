"""Generated from Smithy shape ``com.amazonaws.quicksight#Ingestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.error_info
    import capo_quicksight.types.ingestion_id
    import capo_quicksight.types.ingestion_request_source
    import capo_quicksight.types.ingestion_request_type
    import capo_quicksight.types.ingestion_status
    import capo_quicksight.types.long
    import capo_quicksight.types.queue_info
    import capo_quicksight.types.row_info
    import capo_quicksight.types.timestamp


class Ingestion(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    ingestion_id: NotRequired["capo_quicksight.types.ingestion_id.IngestionId"]
    """<p>Ingestion ID.</p>"""
    ingestion_status: "capo_quicksight.types.ingestion_status.IngestionStatus"
    """<p>Ingestion status.</p>"""
    error_info: NotRequired["capo_quicksight.types.error_info.ErrorInfo"]
    """<p>Error information for this ingestion.</p>"""
    row_info: NotRequired["capo_quicksight.types.row_info.RowInfo"]
    queue_info: NotRequired["capo_quicksight.types.queue_info.QueueInfo"]
    created_time: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The time that this ingestion started.</p>"""
    ingestion_time_in_seconds: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The time that this ingestion took, measured in seconds.</p>"""
    ingestion_size_in_bytes: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The size of the data ingested, in bytes.</p>"""
    request_source: NotRequired[
        "capo_quicksight.types.ingestion_request_source.IngestionRequestSource"
    ]
    """<p>Event source for this ingestion.</p>"""
    request_type: NotRequired[
        "capo_quicksight.types.ingestion_request_type.IngestionRequestType"
    ]
    """<p>Type of this ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ingestion) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "ingestion_id" in value:
        out["IngestionId"] = value["ingestion_id"]
    import capo_quicksight.types.ingestion_status

    out["IngestionStatus"] = capo_quicksight.types.ingestion_status.serialize_json(
        value["ingestion_status"]
    )
    if "error_info" in value:
        import capo_quicksight.types.error_info

        out["ErrorInfo"] = capo_quicksight.types.error_info.serialize_json(
            value["error_info"]
        )
    if "row_info" in value:
        import capo_quicksight.types.row_info

        out["RowInfo"] = capo_quicksight.types.row_info.serialize_json(
            value["row_info"]
        )
    if "queue_info" in value:
        import capo_quicksight.types.queue_info

        out["QueueInfo"] = capo_quicksight.types.queue_info.serialize_json(
            value["queue_info"]
        )
    import capo_quicksight.types.timestamp

    out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_time"]
    )
    if "ingestion_time_in_seconds" in value:
        out["IngestionTimeInSeconds"] = value["ingestion_time_in_seconds"]
    if "ingestion_size_in_bytes" in value:
        out["IngestionSizeInBytes"] = value["ingestion_size_in_bytes"]
    if "request_source" in value:
        import capo_quicksight.types.ingestion_request_source

        out["RequestSource"] = (
            capo_quicksight.types.ingestion_request_source.serialize_json(
                value["request_source"]
            )
        )
    if "request_type" in value:
        import capo_quicksight.types.ingestion_request_type

        out["RequestType"] = (
            capo_quicksight.types.ingestion_request_type.serialize_json(
                value["request_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ingestion:
    out: Ingestion = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Ingestion.arn required")
    if "IngestionId" in data:
        out["ingestion_id"] = data["IngestionId"]
    if "IngestionStatus" in data:
        import capo_quicksight.types.ingestion_status

        out["ingestion_status"] = (
            capo_quicksight.types.ingestion_status.deserialize_json(
                data["IngestionStatus"]
            )
        )
    else:
        raise DeserializationError("Ingestion.ingestion_status required")
    if "ErrorInfo" in data:
        import capo_quicksight.types.error_info

        out["error_info"] = capo_quicksight.types.error_info.deserialize_json(
            data["ErrorInfo"]
        )
    if "RowInfo" in data:
        import capo_quicksight.types.row_info

        out["row_info"] = capo_quicksight.types.row_info.deserialize_json(
            data["RowInfo"]
        )
    if "QueueInfo" in data:
        import capo_quicksight.types.queue_info

        out["queue_info"] = capo_quicksight.types.queue_info.deserialize_json(
            data["QueueInfo"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("Ingestion.created_time required")
    if "IngestionTimeInSeconds" in data:
        out["ingestion_time_in_seconds"] = data["IngestionTimeInSeconds"]
    if "IngestionSizeInBytes" in data:
        out["ingestion_size_in_bytes"] = data["IngestionSizeInBytes"]
    if "RequestSource" in data:
        import capo_quicksight.types.ingestion_request_source

        out["request_source"] = (
            capo_quicksight.types.ingestion_request_source.deserialize_json(
                data["RequestSource"]
            )
        )
    if "RequestType" in data:
        import capo_quicksight.types.ingestion_request_type

        out["request_type"] = (
            capo_quicksight.types.ingestion_request_type.deserialize_json(
                data["RequestType"]
            )
        )
    return out
