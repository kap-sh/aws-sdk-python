"""Generated from Smithy shape ``com.amazonaws.ivs#StreamKeySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_arn
    import aws_sdk_ivs.types.stream_key_arn
    import aws_sdk_ivs.types.tags


class StreamKeySummary(TypedDict):
    arn: NotRequired["aws_sdk_ivs.types.stream_key_arn.StreamKeyArn"]
    """<p>Stream-key ARN.</p>"""
    channel_arn: NotRequired["aws_sdk_ivs.types.channel_arn.ChannelArn"]
    """<p>Channel ARN for the stream.</p>"""
    tags: NotRequired["aws_sdk_ivs.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamKeySummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "tags" in value:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StreamKeySummary:
    out: StreamKeySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    if "tags" in data:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.deserialize_json(data["tags"])
    return out
