"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.resource_tags
    import aws_sdk_kinesis_video.types.stream_name


class TagStreamInput(TypedDict, closed=True):
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags to.</p>"""
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream that you want to add the tag or tags to.</p>"""
    tags: "aws_sdk_kinesis_video.types.resource_tags.ResourceTags"
    """<p>A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagStreamInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import aws_sdk_kinesis_video.types.resource_tags

    out["Tags"] = aws_sdk_kinesis_video.types.resource_tags.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagStreamInput:
    out: TagStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "Tags" in data:
        import aws_sdk_kinesis_video.types.resource_tags

        out["tags"] = aws_sdk_kinesis_video.types.resource_tags.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagStreamInput.tags required")
    return out
