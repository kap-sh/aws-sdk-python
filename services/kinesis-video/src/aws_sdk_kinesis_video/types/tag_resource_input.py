"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel to which you want to add tags.</p>"""
    tags: "aws_sdk_kinesis_video.types.tag_list.TagList"
    """<p>A list of tags to associate with the specified signaling channel. Each tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_kinesis_video.types.tag_list

    out["Tags"] = aws_sdk_kinesis_video.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_kinesis_video.types.tag_list

        out["tags"] = aws_sdk_kinesis_video.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
