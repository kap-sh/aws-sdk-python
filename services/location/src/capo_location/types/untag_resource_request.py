"""Generated from Smithy shape ``com.amazonaws.location#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>"""
    tag_keys: "capo_location.types.tag_keys.TagKeys"
    """<p>The list of tag keys to remove from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
