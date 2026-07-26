"""Generated from Smithy shape ``com.amazonaws.workmail#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.amazon_resource_name
    import capo_workmail.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_workmail.types.amazon_resource_name.AmazonResourceName"
    """<p>The resource ARN.</p>"""
    tags: "capo_workmail.types.tag_list.TagList"
    """<p>The tag key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_workmail.types.tag_list

    out["Tags"] = capo_workmail.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_workmail.types.tag_list

        out["tags"] = capo_workmail.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
