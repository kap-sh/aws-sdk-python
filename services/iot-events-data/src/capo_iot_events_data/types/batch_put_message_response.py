"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchPutMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.batch_put_message_error_entries


class BatchPutMessageResponse(TypedDict, closed=True):
    batch_put_message_error_entries: NotRequired[
        "capo_iot_events_data.types.batch_put_message_error_entries.BatchPutMessageErrorEntries"
    ]
    """<p>A list of any errors encountered when sending the messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMessageResponse) -> dict:
    out: dict = {}
    if "batch_put_message_error_entries" in value:
        import capo_iot_events_data.types.batch_put_message_error_entries

        out["BatchPutMessageErrorEntries"] = (
            capo_iot_events_data.types.batch_put_message_error_entries.serialize_json(
                value["batch_put_message_error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutMessageResponse:
    out: BatchPutMessageResponse = {}  # type: ignore[typeddict-item]
    if "BatchPutMessageErrorEntries" in data:
        import capo_iot_events_data.types.batch_put_message_error_entries

        out["batch_put_message_error_entries"] = (
            capo_iot_events_data.types.batch_put_message_error_entries.deserialize_json(
                data["BatchPutMessageErrorEntries"]
            )
        )
    return out
