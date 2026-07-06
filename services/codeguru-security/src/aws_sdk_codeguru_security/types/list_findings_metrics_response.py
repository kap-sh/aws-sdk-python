"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ListFindingsMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.findings_metric_list
    import aws_sdk_codeguru_security.types.next_token


class ListFindingsMetricsResponse(TypedDict, closed=True):
    findings_metrics: NotRequired[
        "aws_sdk_codeguru_security.types.findings_metric_list.FindingsMetricList"
    ]
    """<p>A list of <code>AccountFindingsMetric</code> objects retrieved from the specified time interval.</p>"""
    next_token: NotRequired["aws_sdk_codeguru_security.types.next_token.NextToken"]
    """<p>A pagination token. You can use this in future calls to <code>ListFindingMetrics</code> to continue listing results after the current page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsMetricsResponse) -> dict:
    out: dict = {}
    if "findings_metrics" in value:
        import aws_sdk_codeguru_security.types.findings_metric_list

        out["findingsMetrics"] = (
            aws_sdk_codeguru_security.types.findings_metric_list.serialize_json(
                value["findings_metrics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsMetricsResponse:
    out: ListFindingsMetricsResponse = {}  # type: ignore[typeddict-item]
    if "findingsMetrics" in data:
        import aws_sdk_codeguru_security.types.findings_metric_list

        out["findings_metrics"] = (
            aws_sdk_codeguru_security.types.findings_metric_list.deserialize_json(
                data["findingsMetrics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
