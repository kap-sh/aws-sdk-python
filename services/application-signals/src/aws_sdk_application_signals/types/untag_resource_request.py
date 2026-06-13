"""Generated from Smithy shape ``com.amazonaws.applicationsignals#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.amazon_resource_name
    import aws_sdk_application_signals.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_application_signals.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to delete tags from.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tag_keys: "aws_sdk_application_signals.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_application_signals.types.tag_key_list

    out["TagKeys"] = aws_sdk_application_signals.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_application_signals.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_application_signals.types.tag_key_list.deserialize_json(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
