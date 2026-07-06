"""Generated from Smithy shape ``com.amazonaws.iot#DeleteFleetMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.fleet_metric_name
    import aws_sdk_iot.types.optional_version


class DeleteFleetMetricRequest(TypedDict, closed=True):
    metric_name: "aws_sdk_iot.types.fleet_metric_name.FleetMetricName"
    """<p>The name of the fleet metric to delete.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the fleet metric to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFleetMetricRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFleetMetricRequest:
    out: DeleteFleetMetricRequest = {}  # type: ignore[typeddict-item]
    return out
