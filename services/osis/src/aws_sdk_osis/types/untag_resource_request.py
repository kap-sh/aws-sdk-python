"""Generated from Smithy shape ``com.amazonaws.osis#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.string_list


class UntagResourceRequest(TypedDict):
    arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the pipeline to remove tags from.</p>"""
    tag_keys: "aws_sdk_osis.types.string_list.StringList"
    """<p>The tag keys to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_osis.types.string_list

    out["TagKeys"] = aws_sdk_osis.types.string_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "TagKeys" in data:
        import aws_sdk_osis.types.string_list

        out["tag_keys"] = aws_sdk_osis.types.string_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
