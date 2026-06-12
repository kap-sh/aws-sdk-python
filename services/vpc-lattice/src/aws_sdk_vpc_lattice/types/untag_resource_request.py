"""Generated from Smithy shape ``com.amazonaws.vpclattice#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.arn
    import aws_sdk_vpc_lattice.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_vpc_lattice.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_vpc_lattice.types.tag_keys.TagKeys"
    """<p>The tag keys of the tags to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
