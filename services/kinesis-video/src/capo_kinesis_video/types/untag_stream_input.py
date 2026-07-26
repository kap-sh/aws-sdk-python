"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UntagStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.tag_key_list


class UntagStreamInput(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream that you want to remove tags from.</p>"""
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream that you want to remove tags from.</p>"""
    tag_key_list: "capo_kinesis_video.types.tag_key_list.TagKeyList"
    """<p>A list of the keys of the tags that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagStreamInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import capo_kinesis_video.types.tag_key_list

    out["TagKeyList"] = capo_kinesis_video.types.tag_key_list.serialize_json(
        value["tag_key_list"]
    )
    return out


def deserialize_json(data: dict) -> UntagStreamInput:
    out: UntagStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "TagKeyList" in data:
        import capo_kinesis_video.types.tag_key_list

        out["tag_key_list"] = capo_kinesis_video.types.tag_key_list.deserialize_json(
            data["TagKeyList"]
        )
    else:
        raise DeserializationError("UntagStreamInput.tag_key_list required")
    return out
