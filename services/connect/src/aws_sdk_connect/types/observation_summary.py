"""Generated from Smithy shape ``com.amazonaws.connect#ObservationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.count


class ObservationSummary(TypedDict, closed=True):
    total_observations: NotRequired["aws_sdk_connect.types.count.Count"]
    """<p>The total number of observations in the test case.</p>"""
    observations_passed: NotRequired["aws_sdk_connect.types.count.Count"]
    """<p>The number of observations that passed during execution.</p>"""
    observations_failed: NotRequired["aws_sdk_connect.types.count.Count"]
    """<p>The number of observations that failed during execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObservationSummary) -> dict:
    out: dict = {}
    if "total_observations" in value:
        out["TotalObservations"] = value["total_observations"]
    if "observations_passed" in value:
        out["ObservationsPassed"] = value["observations_passed"]
    if "observations_failed" in value:
        out["ObservationsFailed"] = value["observations_failed"]
    return out


def deserialize_json(data: dict) -> ObservationSummary:
    out: ObservationSummary = {}  # type: ignore[typeddict-item]
    if "TotalObservations" in data:
        out["total_observations"] = data["TotalObservations"]
    if "ObservationsPassed" in data:
        out["observations_passed"] = data["ObservationsPassed"]
    if "ObservationsFailed" in data:
        out["observations_failed"] = data["ObservationsFailed"]
    return out
