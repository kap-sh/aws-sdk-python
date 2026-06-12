"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateProductRestEndpointPageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.endpoint_display_content
    import aws_sdk_apigatewayv2.types.try_it_state


class UpdateProductRestEndpointPageRequest(TypedDict):
    display_content: NotRequired[
        "aws_sdk_apigatewayv2.types.endpoint_display_content.EndpointDisplayContent"
    ]
    """<p>The display content.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    product_rest_endpoint_page_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The product REST endpoint identifier.</p>"""
    try_it_state: NotRequired["aws_sdk_apigatewayv2.types.try_it_state.TryItState"]
    """<p>The try it state of a product REST endpoint page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProductRestEndpointPageRequest) -> dict:
    out: dict = {}
    if "display_content" in value:
        import aws_sdk_apigatewayv2.types.endpoint_display_content

        out["displayContent"] = (
            aws_sdk_apigatewayv2.types.endpoint_display_content.serialize_json(
                value["display_content"]
            )
        )
    if "try_it_state" in value:
        import aws_sdk_apigatewayv2.types.try_it_state

        out["tryItState"] = aws_sdk_apigatewayv2.types.try_it_state.serialize_json(
            value["try_it_state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProductRestEndpointPageRequest:
    out: UpdateProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
    if "displayContent" in data:
        import aws_sdk_apigatewayv2.types.endpoint_display_content

        out["display_content"] = (
            aws_sdk_apigatewayv2.types.endpoint_display_content.deserialize_json(
                data["displayContent"]
            )
        )
    if "tryItState" in data:
        import aws_sdk_apigatewayv2.types.try_it_state

        out["try_it_state"] = aws_sdk_apigatewayv2.types.try_it_state.deserialize_json(
            data["tryItState"]
        )
    return out
