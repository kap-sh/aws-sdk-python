"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_report_s3_report_list
    import capo_fis.types.experiment_report_state


class ExperimentReport(TypedDict, closed=True):
    state: NotRequired["capo_fis.types.experiment_report_state.ExperimentReportState"]
    """<p>The state of the experiment report.</p>"""
    s3_reports: NotRequired[
        "capo_fis.types.experiment_report_s3_report_list.ExperimentReportS3ReportList"
    ]
    """<p>The S3 destination of the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReport) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_fis.types.experiment_report_state

        out["state"] = capo_fis.types.experiment_report_state.serialize_json(
            value["state"]
        )
    if "s3_reports" in value:
        import capo_fis.types.experiment_report_s3_report_list

        out["s3Reports"] = (
            capo_fis.types.experiment_report_s3_report_list.serialize_json(
                value["s3_reports"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentReport:
    out: ExperimentReport = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_fis.types.experiment_report_state

        out["state"] = capo_fis.types.experiment_report_state.deserialize_json(
            data["state"]
        )
    if "s3Reports" in data:
        import capo_fis.types.experiment_report_s3_report_list

        out["s3_reports"] = (
            capo_fis.types.experiment_report_s3_report_list.deserialize_json(
                data["s3Reports"]
            )
        )
    return out
