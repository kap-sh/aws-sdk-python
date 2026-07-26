"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCustomMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.metric_name


class DeleteCustomMetricRequest(TypedDict, closed=True):
    metric_name: "capo_iot.types.metric_name.MetricName"
    """<p> The name of the custom metric. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomMetricRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomMetricRequest:
    out: DeleteCustomMetricRequest = {}  # type: ignore[typeddict-item]
    return out
