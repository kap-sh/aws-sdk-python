"""Generated from Smithy shape ``com.amazonaws.securityir#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.arn


class ListTagsForResourceInput(TypedDict):
    resource_arn: "aws_sdk_security_ir.types.arn.Arn"
    """<p>Required element for ListTagsForResource to provide the ARN to identify a specific resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
