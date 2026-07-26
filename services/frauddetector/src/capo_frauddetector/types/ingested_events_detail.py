"""Generated from Smithy shape ``com.amazonaws.frauddetector#IngestedEventsDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.ingested_events_time_window


class IngestedEventsDetail(TypedDict, closed=True):
    ingested_events_time_window: (
        "capo_frauddetector.types.ingested_events_time_window.IngestedEventsTimeWindow"
    )
    """<p>The start and stop time of the ingested events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngestedEventsDetail) -> dict:
    out: dict = {}
    import capo_frauddetector.types.ingested_events_time_window

    out["ingestedEventsTimeWindow"] = (
        capo_frauddetector.types.ingested_events_time_window.serialize_aws_json_1_1(
            value["ingested_events_time_window"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IngestedEventsDetail:
    out: IngestedEventsDetail = {}  # type: ignore[typeddict-item]
    if "ingestedEventsTimeWindow" in data:
        import capo_frauddetector.types.ingested_events_time_window

        out["ingested_events_time_window"] = (
            capo_frauddetector.types.ingested_events_time_window.deserialize_aws_json_1_1(
                data["ingestedEventsTimeWindow"]
            )
        )
    else:
        raise DeserializationError(
            "IngestedEventsDetail.ingested_events_time_window required"
        )
    return out
