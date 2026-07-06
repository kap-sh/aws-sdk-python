"""Generated from Smithy shape ``com.amazonaws.mediatailor#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    tags: "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
    r"""<p>The tags to assign to the resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.__map_of__string

    out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
