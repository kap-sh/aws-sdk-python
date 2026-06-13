"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_pinpoint_sms_voice_v2.types.tag_key_list.TagKeyList"
    """<p>An array of tag key values to unassociate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_key_list

    out["TagKeys"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
