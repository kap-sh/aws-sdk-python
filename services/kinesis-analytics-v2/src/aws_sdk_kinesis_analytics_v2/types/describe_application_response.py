"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_detail


class DescribeApplicationResponse(TypedDict, closed=True):
    application_detail: (
        "aws_sdk_kinesis_analytics_v2.types.application_detail.ApplicationDetail"
    )
    """<p>Provides a description of the application, such as the application's Amazon Resource Name (ARN), status, and latest version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationResponse) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.application_detail

    out["ApplicationDetail"] = (
        aws_sdk_kinesis_analytics_v2.types.application_detail.serialize_aws_json_1_1(
            value["application_detail"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationResponse:
    out: DescribeApplicationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationDetail" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_detail

        out["application_detail"] = (
            aws_sdk_kinesis_analytics_v2.types.application_detail.deserialize_aws_json_1_1(
                data["ApplicationDetail"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeApplicationResponse.application_detail required"
        )
    return out
