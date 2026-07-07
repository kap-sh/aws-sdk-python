"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ErrorReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.s3_configuration


class ErrorReportConfiguration(TypedDict, closed=True):
    s3_configuration: "aws_sdk_timestream_query.types.s3_configuration.S3Configuration"
    """<p>The S3 configuration for the error reports.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorReportConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_timestream_query.types.s3_configuration

    out["S3Configuration"] = (
        aws_sdk_timestream_query.types.s3_configuration.serialize_aws_json_1_0(
            value["s3_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorReportConfiguration:
    out: ErrorReportConfiguration = {}  # type: ignore[typeddict-item]
    if "S3Configuration" in data:
        import aws_sdk_timestream_query.types.s3_configuration

        out["s3_configuration"] = (
            aws_sdk_timestream_query.types.s3_configuration.deserialize_aws_json_1_0(
                data["S3Configuration"]
            )
        )
    else:
        raise DeserializationError("ErrorReportConfiguration.s3_configuration required")
    return out
