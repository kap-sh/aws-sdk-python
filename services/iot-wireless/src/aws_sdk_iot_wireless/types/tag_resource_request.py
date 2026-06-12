"""Generated from Smithy shape ``com.amazonaws.iotwireless#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.amazon_resource_name
    import aws_sdk_iot_wireless.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_iot_wireless.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource to add tags to.</p>"""
    tags: "aws_sdk_iot_wireless.types.tag_list.TagList"
    """<p>Adds to or modifies the tags of the given resource. Tags are metadata that you can use to manage a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.tag_list

    out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
