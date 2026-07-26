"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AntipatternReportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.analyzer_name_union
    import capo_migrationhubstrategy.types.antipattern_report_status
    import capo_migrationhubstrategy.types.s3_object
    import capo_migrationhubstrategy.types.status_message


class AntipatternReportResult(TypedDict, closed=True):
    analyzer_name: NotRequired[
        "capo_migrationhubstrategy.types.analyzer_name_union.AnalyzerNameUnion"
    ]
    """<p>The analyzer name.</p>"""
    anti_pattern_report_s3_object: NotRequired[
        "capo_migrationhubstrategy.types.s3_object.S3Object"
    ]
    antipattern_report_status: NotRequired[
        "capo_migrationhubstrategy.types.antipattern_report_status.AntipatternReportStatus"
    ]
    """<p>The status of the anti-pattern report generation.</p>"""
    antipattern_report_status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p>The status message for the anti-pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntipatternReportResult) -> dict:
    out: dict = {}
    if "analyzer_name" in value:
        import capo_migrationhubstrategy.types.analyzer_name_union

        out["analyzerName"] = (
            capo_migrationhubstrategy.types.analyzer_name_union.serialize_json(
                value["analyzer_name"]
            )
        )
    if "anti_pattern_report_s3_object" in value:
        import capo_migrationhubstrategy.types.s3_object

        out["antiPatternReportS3Object"] = (
            capo_migrationhubstrategy.types.s3_object.serialize_json(
                value["anti_pattern_report_s3_object"]
            )
        )
    if "antipattern_report_status" in value:
        out["antipatternReportStatus"] = value["antipattern_report_status"]
    if "antipattern_report_status_message" in value:
        out["antipatternReportStatusMessage"] = value[
            "antipattern_report_status_message"
        ]
    return out


def deserialize_json(data: dict) -> AntipatternReportResult:
    out: AntipatternReportResult = {}  # type: ignore[typeddict-item]
    if "analyzerName" in data:
        import capo_migrationhubstrategy.types.analyzer_name_union

        out["analyzer_name"] = (
            capo_migrationhubstrategy.types.analyzer_name_union.deserialize_json(
                data["analyzerName"]
            )
        )
    if "antiPatternReportS3Object" in data:
        import capo_migrationhubstrategy.types.s3_object

        out["anti_pattern_report_s3_object"] = (
            capo_migrationhubstrategy.types.s3_object.deserialize_json(
                data["antiPatternReportS3Object"]
            )
        )
    if "antipatternReportStatus" in data:
        out["antipattern_report_status"] = data["antipatternReportStatus"]
    if "antipatternReportStatusMessage" in data:
        out["antipattern_report_status_message"] = data[
            "antipatternReportStatusMessage"
        ]
    return out
