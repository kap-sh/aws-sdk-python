"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#MetricsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_codeguru_security.types.categories_with_most_findings
    import capo_codeguru_security.types.finding_metrics_value_per_severity
    import capo_codeguru_security.types.scans_with_most_open_critical_findings
    import capo_codeguru_security.types.scans_with_most_open_findings


class MetricsSummary(TypedDict, closed=True):
    date: NotRequired["datetime.datetime"]
    """<p>The date from which the metrics summary information was retrieved.</p>"""
    open_findings: NotRequired[
        "capo_codeguru_security.types.finding_metrics_value_per_severity.FindingMetricsValuePerSeverity"
    ]
    """<p>The number of open findings of each severity.</p>"""
    categories_with_most_findings: NotRequired[
        "capo_codeguru_security.types.categories_with_most_findings.CategoriesWithMostFindings"
    ]
    """<p>A list of <code>CategoryWithFindingNum</code> objects for the top 5 finding categories with the most findings.</p>"""
    scans_with_most_open_findings: NotRequired[
        "capo_codeguru_security.types.scans_with_most_open_findings.ScansWithMostOpenFindings"
    ]
    """<p>A list of <code>ScanNameWithFindingNum</code> objects for the top 3 scans with the most number of open findings.</p>"""
    scans_with_most_open_critical_findings: NotRequired[
        "capo_codeguru_security.types.scans_with_most_open_critical_findings.ScansWithMostOpenCriticalFindings"
    ]
    """<p>A list of <code>ScanNameWithFindingNum</code> objects for the top 3 scans with the most number of open critical findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsSummary) -> dict:
    out: dict = {}
    if "date" in value:
        import capo_codeguru_security.types._prelude.timestamp

        out["date"] = capo_codeguru_security.types._prelude.timestamp.serialize_json(
            value["date"]
        )
    if "open_findings" in value:
        import capo_codeguru_security.types.finding_metrics_value_per_severity

        out["openFindings"] = (
            capo_codeguru_security.types.finding_metrics_value_per_severity.serialize_json(
                value["open_findings"]
            )
        )
    if "categories_with_most_findings" in value:
        import capo_codeguru_security.types.categories_with_most_findings

        out["categoriesWithMostFindings"] = (
            capo_codeguru_security.types.categories_with_most_findings.serialize_json(
                value["categories_with_most_findings"]
            )
        )
    if "scans_with_most_open_findings" in value:
        import capo_codeguru_security.types.scans_with_most_open_findings

        out["scansWithMostOpenFindings"] = (
            capo_codeguru_security.types.scans_with_most_open_findings.serialize_json(
                value["scans_with_most_open_findings"]
            )
        )
    if "scans_with_most_open_critical_findings" in value:
        import capo_codeguru_security.types.scans_with_most_open_critical_findings

        out["scansWithMostOpenCriticalFindings"] = (
            capo_codeguru_security.types.scans_with_most_open_critical_findings.serialize_json(
                value["scans_with_most_open_critical_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricsSummary:
    out: MetricsSummary = {}  # type: ignore[typeddict-item]
    if "date" in data:
        import capo_codeguru_security.types._prelude.timestamp

        out["date"] = capo_codeguru_security.types._prelude.timestamp.deserialize_json(
            data["date"]
        )
    if "openFindings" in data:
        import capo_codeguru_security.types.finding_metrics_value_per_severity

        out["open_findings"] = (
            capo_codeguru_security.types.finding_metrics_value_per_severity.deserialize_json(
                data["openFindings"]
            )
        )
    if "categoriesWithMostFindings" in data:
        import capo_codeguru_security.types.categories_with_most_findings

        out["categories_with_most_findings"] = (
            capo_codeguru_security.types.categories_with_most_findings.deserialize_json(
                data["categoriesWithMostFindings"]
            )
        )
    if "scansWithMostOpenFindings" in data:
        import capo_codeguru_security.types.scans_with_most_open_findings

        out["scans_with_most_open_findings"] = (
            capo_codeguru_security.types.scans_with_most_open_findings.deserialize_json(
                data["scansWithMostOpenFindings"]
            )
        )
    if "scansWithMostOpenCriticalFindings" in data:
        import capo_codeguru_security.types.scans_with_most_open_critical_findings

        out["scans_with_most_open_critical_findings"] = (
            capo_codeguru_security.types.scans_with_most_open_critical_findings.deserialize_json(
                data["scansWithMostOpenCriticalFindings"]
            )
        )
    return out
