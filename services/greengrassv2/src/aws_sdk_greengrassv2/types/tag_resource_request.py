"""Generated from Smithy shape ``com.amazonaws.greengrassv2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.generic_v2_arn
    import aws_sdk_greengrassv2.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_greengrassv2.types.generic_v2_arn.GenericV2ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the resource to tag.</p>"""
    tags: "aws_sdk_greengrassv2.types.tag_map.TagMap"
    r"""<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html\">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_greengrassv2.types.tag_map

    out["tags"] = aws_sdk_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_greengrassv2.types.tag_map

        out["tags"] = aws_sdk_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
