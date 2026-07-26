"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Batch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.timestamp


class Batch(TypedDict, closed=True):
    start_time: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Start time of batch to split ingestion.</p>"""
    end_time: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>End time of batch to split ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Batch) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.timestamp

    out["StartTime"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_customer_profiles.types.timestamp

    out["EndTime"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> Batch:
    out: Batch = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_customer_profiles.types.timestamp

        out["start_time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("Batch.start_time required")
    if "EndTime" in data:
        import capo_customer_profiles.types.timestamp

        out["end_time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    else:
        raise DeserializationError("Batch.end_time required")
    return out
