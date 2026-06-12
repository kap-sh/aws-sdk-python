"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.amazon_resource_name
    import aws_sdk_application_insights.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_application_insights.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the application that you want to remove one or more tags from.</p>"""
    tag_keys: "aws_sdk_application_insights.types.tag_key_list.TagKeyList"
    """<p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the application, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_application_insights.types.tag_key_list

    out["TagKeys"] = (
        aws_sdk_application_insights.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_application_insights.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_application_insights.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
