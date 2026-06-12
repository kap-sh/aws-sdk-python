"""Generated from Smithy shape ``com.amazonaws.schemas#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__list_of__string
    import aws_sdk_schemas.types.__string


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_schemas.types.__string.__string"
    """<p>The ARN of the resource.</p>"""
    tag_keys: NotRequired["aws_sdk_schemas.types.__list_of__string.__listOf__string"]
    """<p>Keys of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
