"""Generated from Smithy shape ``com.amazonaws.b2bi#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.amazon_resource_name
    import aws_sdk_b2bi.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_b2bi.types.amazon_resource_name.AmazonResourceName"
    """<p>Specifies an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    tags: "aws_sdk_b2bi.types.tag_list.TagList"
    """<p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.tag_list

    out["Tags"] = aws_sdk_b2bi.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.deserialize_aws_json_1_0(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
