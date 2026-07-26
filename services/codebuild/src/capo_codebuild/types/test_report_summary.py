"""Generated from Smithy shape ``com.amazonaws.codebuild#TestReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.report_status_counts
    import capo_codebuild.types.wrapper_int
    import capo_codebuild.types.wrapper_long


class TestReportSummary(TypedDict, closed=True):
    total: "capo_codebuild.types.wrapper_int.WrapperInt"
    """<p> The number of test cases in this <code>TestReportSummary</code>. The total includes truncated test cases. </p>"""
    status_counts: "capo_codebuild.types.report_status_counts.ReportStatusCounts"
    """<p> A map that contains the number of each type of status returned by the test results in this <code>TestReportSummary</code>. </p>"""
    duration_in_nano_seconds: "capo_codebuild.types.wrapper_long.WrapperLong"
    """<p> The number of nanoseconds it took to run all of the test cases in this report. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestReportSummary) -> dict:
    out: dict = {}
    out["total"] = value["total"]
    import capo_codebuild.types.report_status_counts

    out["statusCounts"] = (
        capo_codebuild.types.report_status_counts.serialize_aws_json_1_1(
            value["status_counts"]
        )
    )
    out["durationInNanoSeconds"] = value["duration_in_nano_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestReportSummary:
    out: TestReportSummary = {}  # type: ignore[typeddict-item]
    if "total" in data:
        out["total"] = data["total"]
    else:
        raise DeserializationError("TestReportSummary.total required")
    if "statusCounts" in data:
        import capo_codebuild.types.report_status_counts

        out["status_counts"] = (
            capo_codebuild.types.report_status_counts.deserialize_aws_json_1_1(
                data["statusCounts"]
            )
        )
    else:
        raise DeserializationError("TestReportSummary.status_counts required")
    if "durationInNanoSeconds" in data:
        out["duration_in_nano_seconds"] = data["durationInNanoSeconds"]
    else:
        raise DeserializationError(
            "TestReportSummary.duration_in_nano_seconds required"
        )
    return out
