"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanConfigurationContinuousScanDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_guardduty.errors import DeserializationError

if TYPE_CHECKING:
    import capo_guardduty.types.timestamp


class ScanConfigurationContinuousScanDetails(TypedDict, closed=True):
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp representing the start of the time range that was scanned.</p>"""
    end_time: "capo_guardduty.types.timestamp.Timestamp"
    """<p>The timestamp representing the end of the time range that was scanned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanConfigurationContinuousScanDetails) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    import capo_guardduty.types.timestamp

    out["endTime"] = capo_guardduty.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> ScanConfigurationContinuousScanDetails:
    out: ScanConfigurationContinuousScanDetails = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_guardduty.types.timestamp

        out["start_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_guardduty.types.timestamp

        out["end_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError(
            "ScanConfigurationContinuousScanDetails.end_time required"
        )
    return out
