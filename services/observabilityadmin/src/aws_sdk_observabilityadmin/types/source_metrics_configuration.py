"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SourceMetricsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.metrics_filter_string


class SourceMetricsConfiguration(TypedDict):
    metrics_selection_criteria: NotRequired[
        "aws_sdk_observabilityadmin.types.metrics_filter_string.MetricsFilterString"
    ]
    """<p>The filter expression that selects which source metrics to centralize. Currently, only <code>*</code> (all metrics) is supported. Other values return a validation error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceMetricsConfiguration) -> dict:
    out: dict = {}
    if "metrics_selection_criteria" in value:
        out["MetricsSelectionCriteria"] = value["metrics_selection_criteria"]
    return out


def deserialize_json(data: dict) -> SourceMetricsConfiguration:
    out: SourceMetricsConfiguration = {}  # type: ignore[typeddict-item]
    if "MetricsSelectionCriteria" in data:
        out["metrics_selection_criteria"] = data["MetricsSelectionCriteria"]
    return out
