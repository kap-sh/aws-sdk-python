"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.kinesis_analytics_arn
    import capo_kinesis_analytics_v2.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_kinesis_analytics_v2.types.kinesis_analytics_arn.KinesisAnalyticsARN"
    )
    """<p>The ARN of the application to assign the tags.</p>"""
    tags: "capo_kinesis_analytics_v2.types.tags.Tags"
    """<p>The key-value tags to assign to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kinesis_analytics_v2.types.tags

    out["Tags"] = capo_kinesis_analytics_v2.types.tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_kinesis_analytics_v2.types.tags

        out["tags"] = capo_kinesis_analytics_v2.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
