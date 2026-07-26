"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#GetMetricsSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.metrics_summary


class GetMetricsSummaryResponse(TypedDict, closed=True):
    metrics_summary: NotRequired[
        "capo_codeguru_security.types.metrics_summary.MetricsSummary"
    ]
    """<p>The summary metrics from the specified date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricsSummaryResponse) -> dict:
    out: dict = {}
    if "metrics_summary" in value:
        import capo_codeguru_security.types.metrics_summary

        out["metricsSummary"] = (
            capo_codeguru_security.types.metrics_summary.serialize_json(
                value["metrics_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetricsSummaryResponse:
    out: GetMetricsSummaryResponse = {}  # type: ignore[typeddict-item]
    if "metricsSummary" in data:
        import capo_codeguru_security.types.metrics_summary

        out["metrics_summary"] = (
            capo_codeguru_security.types.metrics_summary.deserialize_json(
                data["metricsSummary"]
            )
        )
    return out
