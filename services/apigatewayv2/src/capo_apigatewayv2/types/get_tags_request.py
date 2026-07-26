"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetTagsRequest(TypedDict, closed=True):
    resource_arn: "capo_apigatewayv2.types.__string.__string"
    """<p>The resource ARN for the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTagsRequest:
    out: GetTagsRequest = {}  # type: ignore[typeddict-item]
    return out
