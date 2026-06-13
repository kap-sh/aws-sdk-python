"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#AccountFindingsMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity


class AccountFindingsMetric(TypedDict):
    date: NotRequired["datetime.datetime"]
    """<p>The date from which the findings metrics were retrieved.</p>"""
    new_findings: NotRequired[
        "aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.FindingMetricsValuePerSeverity"
    ]
    """<p>The number of new findings of each severity on the specified date.</p>"""
    closed_findings: NotRequired[
        "aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.FindingMetricsValuePerSeverity"
    ]
    """<p>The number of closed findings of each severity on the specified date.</p>"""
    open_findings: NotRequired[
        "aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.FindingMetricsValuePerSeverity"
    ]
    """<p>The number of open findings of each severity as of the specified date.</p>"""
    mean_time_to_close: NotRequired[
        "aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.FindingMetricsValuePerSeverity"
    ]
    """<p>The average time in days it takes to close findings of each severity as of a specified date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountFindingsMetric) -> dict:
    out: dict = {}
    if "date" in value:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["date"] = aws_sdk_codeguru_security.types._prelude.timestamp.serialize_json(
            value["date"]
        )
    if "new_findings" in value:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["newFindings"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.serialize_json(
                value["new_findings"]
            )
        )
    if "closed_findings" in value:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["closedFindings"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.serialize_json(
                value["closed_findings"]
            )
        )
    if "open_findings" in value:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["openFindings"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.serialize_json(
                value["open_findings"]
            )
        )
    if "mean_time_to_close" in value:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["meanTimeToClose"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.serialize_json(
                value["mean_time_to_close"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountFindingsMetric:
    out: AccountFindingsMetric = {}  # type: ignore[typeddict-item]
    if "date" in data:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["date"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["date"]
            )
        )
    if "newFindings" in data:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["new_findings"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.deserialize_json(
                data["newFindings"]
            )
        )
    if "closedFindings" in data:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["closed_findings"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.deserialize_json(
                data["closedFindings"]
            )
        )
    if "openFindings" in data:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["open_findings"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.deserialize_json(
                data["openFindings"]
            )
        )
    if "meanTimeToClose" in data:
        import aws_sdk_codeguru_security.types.finding_metrics_value_per_severity

        out["mean_time_to_close"] = (
            aws_sdk_codeguru_security.types.finding_metrics_value_per_severity.deserialize_json(
                data["meanTimeToClose"]
            )
        )
    return out
