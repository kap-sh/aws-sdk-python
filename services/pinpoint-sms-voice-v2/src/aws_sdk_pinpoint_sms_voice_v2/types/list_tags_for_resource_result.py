"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class ListTagsForResourceResult(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the resource.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
