"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The resource ARN for the tag.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
