"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.audio_segment
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_row
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_type
    import aws_sdk_bedrock_agent_runtime.types.video_segment


class RetrievalResultContent(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_type.RetrievalResultContentType"
    ]
    """<p>The type of content in the retrieval result.</p>"""
    text: "str"
    """<p>The cited text from the data source.</p>"""
    byte_content: NotRequired["str"]
    """<p>A data URI with base64-encoded content from the data source. The URI is in the following format: returned in the following format: <code>data:image/jpeg;base64,${base64-encoded string}</code>.</p>"""
    video: NotRequired["aws_sdk_bedrock_agent_runtime.types.video_segment.VideoSegment"]
    """<p>Video segment information when the retrieval result contains video content.</p>"""
    audio: NotRequired["aws_sdk_bedrock_agent_runtime.types.audio_segment.AudioSegment"]
    """<p>Audio segment information when the retrieval result contains audio content.</p>"""
    row: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_row.RetrievalResultContentRow"
    ]
    """<p>Specifies information about the rows with the cells to return in retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultContent) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_type.serialize_json(
                value["type"]
            )
        )
    out["text"] = value.get("text", "")
    if "byte_content" in value:
        out["byteContent"] = value["byte_content"]
    if "video" in value:
        import aws_sdk_bedrock_agent_runtime.types.video_segment

        out["video"] = aws_sdk_bedrock_agent_runtime.types.video_segment.serialize_json(
            value["video"]
        )
    if "audio" in value:
        import aws_sdk_bedrock_agent_runtime.types.audio_segment

        out["audio"] = aws_sdk_bedrock_agent_runtime.types.audio_segment.serialize_json(
            value["audio"]
        )
    if "row" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_row

        out["row"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_row.serialize_json(
                value["row"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrievalResultContent:
    out: RetrievalResultContent = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_type.deserialize_json(
                data["type"]
            )
        )
    if "text" in data:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if "byteContent" in data:
        out["byte_content"] = data["byteContent"]
    if "video" in data:
        import aws_sdk_bedrock_agent_runtime.types.video_segment

        out["video"] = (
            aws_sdk_bedrock_agent_runtime.types.video_segment.deserialize_json(
                data["video"]
            )
        )
    if "audio" in data:
        import aws_sdk_bedrock_agent_runtime.types.audio_segment

        out["audio"] = (
            aws_sdk_bedrock_agent_runtime.types.audio_segment.deserialize_json(
                data["audio"]
            )
        )
    if "row" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_row

        out["row"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_row.deserialize_json(
                data["row"]
            )
        )
    return out
