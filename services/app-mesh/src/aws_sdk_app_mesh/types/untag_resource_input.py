"""Generated from Smithy shape ``com.amazonaws.appmesh#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.arn
    import aws_sdk_app_mesh.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_app_mesh.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>"""
    tag_keys: "aws_sdk_app_mesh.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.tag_key_list

    out["tagKeys"] = aws_sdk_app_mesh.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "tagKeys" in data:
        import aws_sdk_app_mesh.types.tag_key_list

        out["tag_keys"] = aws_sdk_app_mesh.types.tag_key_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
