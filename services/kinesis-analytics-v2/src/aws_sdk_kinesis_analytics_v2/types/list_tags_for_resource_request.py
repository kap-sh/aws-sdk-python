"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.kinesis_analytics_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_kinesis_analytics_v2.types.kinesis_analytics_arn.KinesisAnalyticsARN"
    )
    """<p>The ARN of the application for which to retrieve tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
