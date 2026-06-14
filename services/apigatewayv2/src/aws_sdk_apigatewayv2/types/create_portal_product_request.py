"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreatePortalProductRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min0_max1024
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.tags


class CreatePortalProductRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """<p>A description of the portal product.</p>"""
    display_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
    ]
    """<p>The name of the portal product as it appears in a published portal.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalProductRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePortalProductRequest:
    out: CreatePortalProductRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
