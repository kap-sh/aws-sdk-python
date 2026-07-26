"""Generated from Smithy shape ``com.amazonaws.apigateway#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_api_gateway.types.string.String"
    """<p>The ARN of a resource that can be tagged.</p>"""
    tag_keys: "capo_api_gateway.types.list_of_string.ListOfString"
    """<p>The Tag keys to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
