"""Generated from Smithy shape ``com.amazonaws.securitylake#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource for which you want to retrieve the tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
