"""Generated from Smithy shape ``com.amazonaws.datazone#EventSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.open_lineage_run_event_summary


class _EventSummary_openLineageRunEventSummary(TypedDict, closed=True):
    openLineageRunEventSummary: (
        "capo_datazone.types.open_lineage_run_event_summary.OpenLineageRunEventSummary"
    )


EventSummary: TypeAlias = _EventSummary_openLineageRunEventSummary


# --- restJson1 ser/de ---
def serialize_json(value: EventSummary) -> dict:
    if "openLineageRunEventSummary" in value:
        import capo_datazone.types.open_lineage_run_event_summary

        return {
            "openLineageRunEventSummary": capo_datazone.types.open_lineage_run_event_summary.serialize_json(
                value["openLineageRunEventSummary"]
            )
        }
    else:
        raise SerializationError("EventSummary: no variant present")


def deserialize_json(data: dict) -> EventSummary:
    if "openLineageRunEventSummary" in data:
        import capo_datazone.types.open_lineage_run_event_summary

        return {
            "openLineageRunEventSummary": capo_datazone.types.open_lineage_run_event_summary.deserialize_json(
                data["openLineageRunEventSummary"]
            )
        }
    else:
        raise DeserializationError("EventSummary: no recognized variant key")
