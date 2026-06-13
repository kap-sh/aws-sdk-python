"""Generated from Smithy shape ``com.amazonaws.location#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
