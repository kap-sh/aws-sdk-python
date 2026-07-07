"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of__string
    import aws_sdk_apigatewayv2.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The resource ARN for the tag.</p>"""
    tag_keys: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string.__listOf__string"
    ]
    """<p>The Tag keys to delete</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
