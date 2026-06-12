"""Generated from Smithy shape ``com.amazonaws.datasync#ReportDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.report_destination_s3


class ReportDestination(TypedDict):
    s3: NotRequired["aws_sdk_datasync.types.report_destination_s3.ReportDestinationS3"]
    """<p>Specifies the Amazon S3 bucket where DataSync uploads your task report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportDestination) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_datasync.types.report_destination_s3

        out["S3"] = aws_sdk_datasync.types.report_destination_s3.serialize_aws_json_1_1(
            value["s3"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportDestination:
    out: ReportDestination = {}  # type: ignore[typeddict-item]
    if "S3" in data:
        import aws_sdk_datasync.types.report_destination_s3

        out["s3"] = (
            aws_sdk_datasync.types.report_destination_s3.deserialize_aws_json_1_1(
                data["S3"]
            )
        )
    return out
