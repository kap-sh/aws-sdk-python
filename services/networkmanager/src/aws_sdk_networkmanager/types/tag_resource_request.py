"""Generated from Smithy shape ``com.amazonaws.networkmanager#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.resource_arn
    import aws_sdk_networkmanager.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_networkmanager.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_networkmanager.types.tag_list.TagList"
    """<p>The tags to apply to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_networkmanager.types.tag_list

    out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
