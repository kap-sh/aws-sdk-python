"""Generated from Smithy shape ``com.amazonaws.applicationsignals#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.amazon_resource_name
    import aws_sdk_application_signals.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_application_signals.types.amazon_resource_name.AmazonResourceName"
    )
    r"""<p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to set tags for.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tags: "aws_sdk_application_signals.types.tag_list.TagList"
    """<p>The list of key-value pairs to associate with the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_application_signals.types.tag_list

    out["Tags"] = aws_sdk_application_signals.types.tag_list.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_application_signals.types.tag_list

        out["tags"] = aws_sdk_application_signals.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
