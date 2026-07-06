"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_detail


class DescribeApplicationVersionResponse(TypedDict, closed=True):
    application_version_detail: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_detail.ApplicationDetail"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationVersionResponse) -> dict:
    out: dict = {}
    if "application_version_detail" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_detail

        out["ApplicationVersionDetail"] = (
            aws_sdk_kinesis_analytics_v2.types.application_detail.serialize_aws_json_1_1(
                value["application_version_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationVersionResponse:
    out: DescribeApplicationVersionResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationVersionDetail" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_detail

        out["application_version_detail"] = (
            aws_sdk_kinesis_analytics_v2.types.application_detail.deserialize_aws_json_1_1(
                data["ApplicationVersionDetail"]
            )
        )
    return out
