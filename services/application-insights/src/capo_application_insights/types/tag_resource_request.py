"""Generated from Smithy shape ``com.amazonaws.applicationinsights#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.amazon_resource_name
    import capo_application_insights.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_application_insights.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the application that you want to add one or more tags to.</p>"""
    tags: "capo_application_insights.types.tag_list.TagList"
    """<p>A list of tags that to add to the application. A tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_application_insights.types.tag_list

    out["Tags"] = capo_application_insights.types.tag_list.serialize_aws_json_1_1(
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
        import capo_application_insights.types.tag_list

        out["tags"] = capo_application_insights.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
