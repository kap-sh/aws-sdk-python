"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ErrorReportLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.s3_report_location


class ErrorReportLocation(TypedDict, closed=True):
    s3_report_location: NotRequired[
        "aws_sdk_timestream_query.types.s3_report_location.S3ReportLocation"
    ]
    """<p>The S3 location where error reports are written.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorReportLocation) -> dict:
    out: dict = {}
    if "s3_report_location" in value:
        import aws_sdk_timestream_query.types.s3_report_location

        out["S3ReportLocation"] = (
            aws_sdk_timestream_query.types.s3_report_location.serialize_aws_json_1_0(
                value["s3_report_location"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorReportLocation:
    out: ErrorReportLocation = {}  # type: ignore[typeddict-item]
    if "S3ReportLocation" in data:
        import aws_sdk_timestream_query.types.s3_report_location

        out["s3_report_location"] = (
            aws_sdk_timestream_query.types.s3_report_location.deserialize_aws_json_1_0(
                data["S3ReportLocation"]
            )
        )
    return out
