"""Generated from Smithy shape ``com.amazonaws.cloudformation#EventFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.failed_events_filter


class EventFilter(TypedDict, closed=True):
    failed_events: NotRequired[
        "capo_cloudformation.types.failed_events_filter.FailedEventsFilter"
    ]
    """<p>When set to true, only returns failed events within the operation. This helps quickly identify root causes for a failed operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "failed_events" in value:
        pairs.append(
            (f"{prefix}.FailedEvents", "true" if value["failed_events"] else "false")
        )


def deserialize_query(el: Element) -> EventFilter:
    out: EventFilter = {}  # type: ignore[typeddict-item]
    child_failed_events = el.find("FailedEvents")
    if child_failed_events is not None:
        out["failed_events"] = (child_failed_events.text or "").lower() == "true"
    return out
