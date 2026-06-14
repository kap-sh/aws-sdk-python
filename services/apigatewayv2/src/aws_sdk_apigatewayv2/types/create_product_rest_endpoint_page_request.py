"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateProductRestEndpointPageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.endpoint_display_content
    import aws_sdk_apigatewayv2.types.rest_endpoint_identifier
    import aws_sdk_apigatewayv2.types.try_it_state


class CreateProductRestEndpointPageRequest(TypedDict):
    display_content: NotRequired[
        "aws_sdk_apigatewayv2.types.endpoint_display_content.EndpointDisplayContent"
    ]
    """<p>The content of the product REST endpoint page.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""
    rest_endpoint_identifier: NotRequired[
        "aws_sdk_apigatewayv2.types.rest_endpoint_identifier.RestEndpointIdentifier"
    ]
    """<p>The REST endpoint identifier.</p>"""
    try_it_state: NotRequired["aws_sdk_apigatewayv2.types.try_it_state.TryItState"]
    """<p>The try it state of the product REST endpoint page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProductRestEndpointPageRequest) -> dict:
    out: dict = {}
    if "display_content" in value:
        import aws_sdk_apigatewayv2.types.endpoint_display_content

        out["displayContent"] = (
            aws_sdk_apigatewayv2.types.endpoint_display_content.serialize_json(
                value["display_content"]
            )
        )
    if "rest_endpoint_identifier" in value:
        import aws_sdk_apigatewayv2.types.rest_endpoint_identifier

        out["restEndpointIdentifier"] = (
            aws_sdk_apigatewayv2.types.rest_endpoint_identifier.serialize_json(
                value["rest_endpoint_identifier"]
            )
        )
    if "try_it_state" in value:
        import aws_sdk_apigatewayv2.types.try_it_state

        out["tryItState"] = aws_sdk_apigatewayv2.types.try_it_state.serialize_json(
            value["try_it_state"]
        )
    return out


def deserialize_json(data: dict) -> CreateProductRestEndpointPageRequest:
    out: CreateProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
    if "displayContent" in data:
        import aws_sdk_apigatewayv2.types.endpoint_display_content

        out["display_content"] = (
            aws_sdk_apigatewayv2.types.endpoint_display_content.deserialize_json(
                data["displayContent"]
            )
        )
    if "restEndpointIdentifier" in data:
        import aws_sdk_apigatewayv2.types.rest_endpoint_identifier

        out["rest_endpoint_identifier"] = (
            aws_sdk_apigatewayv2.types.rest_endpoint_identifier.deserialize_json(
                data["restEndpointIdentifier"]
            )
        )
    if "tryItState" in data:
        import aws_sdk_apigatewayv2.types.try_it_state

        out["try_it_state"] = aws_sdk_apigatewayv2.types.try_it_state.deserialize_json(
            data["tryItState"]
        )
    return out
