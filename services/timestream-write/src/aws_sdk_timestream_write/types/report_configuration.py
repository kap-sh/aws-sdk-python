"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.report_s3_configuration


class ReportConfiguration(TypedDict, closed=True):
    report_s3_configuration: NotRequired[
        "aws_sdk_timestream_write.types.report_s3_configuration.ReportS3Configuration"
    ]
    """<p>Configuration of an S3 location to write error reports and events for a batch load.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportConfiguration) -> dict:
    out: dict = {}
    if "report_s3_configuration" in value:
        import aws_sdk_timestream_write.types.report_s3_configuration

        out["ReportS3Configuration"] = (
            aws_sdk_timestream_write.types.report_s3_configuration.serialize_aws_json_1_0(
                value["report_s3_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReportConfiguration:
    out: ReportConfiguration = {}  # type: ignore[typeddict-item]
    if "ReportS3Configuration" in data:
        import aws_sdk_timestream_write.types.report_s3_configuration

        out["report_s3_configuration"] = (
            aws_sdk_timestream_write.types.report_s3_configuration.deserialize_aws_json_1_0(
                data["ReportS3Configuration"]
            )
        )
    return out
