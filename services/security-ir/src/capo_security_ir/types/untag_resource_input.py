"""Generated from Smithy shape ``com.amazonaws.securityir#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.arn
    import capo_security_ir.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_security_ir.types.arn.Arn"
    """<p>Required element for UnTagResource to identify the ARN for the resource to remove a tag from.</p>"""
    tag_keys: "capo_security_ir.types.tag_keys.TagKeys"
    """<p>Required element for UnTagResource to identify tag to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
