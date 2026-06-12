"""Generated from Smithy shape ``com.amazonaws.mpa#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.string
    import aws_sdk_mpa.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource you want to untag.</p>"""
    tag_keys: "aws_sdk_mpa.types.tag_key_list.TagKeyList"
    """<p>Array of tag key-value pairs that you want to untag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_mpa.types.tag_key_list

    out["TagKeys"] = aws_sdk_mpa.types.tag_key_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "TagKeys" in data:
        import aws_sdk_mpa.types.tag_key_list

        out["tag_keys"] = aws_sdk_mpa.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
