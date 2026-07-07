"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class DeleteApplicationOutputResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    application_version_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The current application version ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationOutputResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationOutputResponse:
    out: DeleteApplicationOutputResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    return out
