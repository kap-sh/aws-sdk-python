"""Generated from Smithy shape ``com.amazonaws.securityir#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.arn
    import aws_sdk_security_ir.types.tag_keys


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_security_ir.types.arn.Arn"
    """<p>Required element for UnTagResource to identify the ARN for the resource to remove a tag from.</p>"""
    tag_keys: "aws_sdk_security_ir.types.tag_keys.TagKeys"
    """<p>Required element for UnTagResource to identify tag to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
