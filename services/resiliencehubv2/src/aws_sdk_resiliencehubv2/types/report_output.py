"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.failed_report_output
    import aws_sdk_resiliencehubv2.types.s3_report_output


class _ReportOutput_s3ReportOutput(TypedDict):
    s3ReportOutput: "aws_sdk_resiliencehubv2.types.s3_report_output.S3ReportOutput"


class _ReportOutput_failedReportOutput(TypedDict):
    failedReportOutput: (
        "aws_sdk_resiliencehubv2.types.failed_report_output.FailedReportOutput"
    )


ReportOutput: TypeAlias = (
    _ReportOutput_s3ReportOutput | _ReportOutput_failedReportOutput
)


# --- restJson1 ser/de ---
def serialize_json(value: ReportOutput) -> dict:
    if "s3ReportOutput" in value:
        import aws_sdk_resiliencehubv2.types.s3_report_output

        return {
            "s3ReportOutput": aws_sdk_resiliencehubv2.types.s3_report_output.serialize_json(
                value["s3ReportOutput"]
            )
        }
    elif "failedReportOutput" in value:
        import aws_sdk_resiliencehubv2.types.failed_report_output

        return {
            "failedReportOutput": aws_sdk_resiliencehubv2.types.failed_report_output.serialize_json(
                value["failedReportOutput"]
            )
        }
    else:
        raise SerializationError("ReportOutput: no variant present")


def deserialize_json(data: dict) -> ReportOutput:
    if "s3ReportOutput" in data:
        import aws_sdk_resiliencehubv2.types.s3_report_output

        return {
            "s3ReportOutput": aws_sdk_resiliencehubv2.types.s3_report_output.deserialize_json(
                data["s3ReportOutput"]
            )
        }
    elif "failedReportOutput" in data:
        import aws_sdk_resiliencehubv2.types.failed_report_output

        return {
            "failedReportOutput": aws_sdk_resiliencehubv2.types.failed_report_output.deserialize_json(
                data["failedReportOutput"]
            )
        }
    else:
        raise DeserializationError("ReportOutput: no recognized variant key")
