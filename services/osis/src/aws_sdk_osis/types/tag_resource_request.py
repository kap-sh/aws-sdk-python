"""Generated from Smithy shape ``com.amazonaws.osis#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the pipeline to tag.</p>"""
    tags: "aws_sdk_osis.types.tag_list.TagList"
    """<p>The list of key-value tags to add to the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_osis.types.tag_list

    out["Tags"] = aws_sdk_osis.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_osis.types.tag_list

        out["tags"] = aws_sdk_osis.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
