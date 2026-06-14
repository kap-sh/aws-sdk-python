"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetProductRestEndpointPageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09
    import aws_sdk_apigatewayv2.types.__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.endpoint_display_content_response
    import aws_sdk_apigatewayv2.types.rest_endpoint_identifier
    import aws_sdk_apigatewayv2.types.status
    import aws_sdk_apigatewayv2.types.status_exception
    import aws_sdk_apigatewayv2.types.try_it_state


class GetProductRestEndpointPageResponse(TypedDict):
    display_content: NotRequired[
        "aws_sdk_apigatewayv2.types.endpoint_display_content_response.EndpointDisplayContentResponse"
    ]
    """<p>The content of the product REST endpoint page.</p>"""
    last_modified: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the product REST endpoint page was last modified.</p>"""
    product_rest_endpoint_page_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The ARN of the product REST endpoint page.</p>"""
    product_rest_endpoint_page_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09.__stringMin10Max30PatternAZ09"
    ]
    """<p>The product REST endpoint page identifier.</p>"""
    raw_display_content: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The raw display content of the product REST endpoint page.</p>"""
    rest_endpoint_identifier: NotRequired[
        "aws_sdk_apigatewayv2.types.rest_endpoint_identifier.RestEndpointIdentifier"
    ]
    """<p>The REST endpoint identifier.</p>"""
    status: NotRequired["aws_sdk_apigatewayv2.types.status.Status"]
    """<p>The status of the product REST endpoint page.</p>"""
    status_exception: NotRequired[
        "aws_sdk_apigatewayv2.types.status_exception.StatusException"
    ]
    """<p>The status exception information.</p>"""
    try_it_state: NotRequired["aws_sdk_apigatewayv2.types.try_it_state.TryItState"]
    """<p>The try it state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductRestEndpointPageResponse) -> dict:
    out: dict = {}
    if "display_content" in value:
        import aws_sdk_apigatewayv2.types.endpoint_display_content_response

        out["displayContent"] = (
            aws_sdk_apigatewayv2.types.endpoint_display_content_response.serialize_json(
                value["display_content"]
            )
        )
    if "last_modified" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["lastModified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_modified"]
            )
        )
    if "product_rest_endpoint_page_arn" in value:
        out["productRestEndpointPageArn"] = value["product_rest_endpoint_page_arn"]
    if "product_rest_endpoint_page_id" in value:
        out["productRestEndpointPageId"] = value["product_rest_endpoint_page_id"]
    if "raw_display_content" in value:
        out["rawDisplayContent"] = value["raw_display_content"]
    if "rest_endpoint_identifier" in value:
        import aws_sdk_apigatewayv2.types.rest_endpoint_identifier

        out["restEndpointIdentifier"] = (
            aws_sdk_apigatewayv2.types.rest_endpoint_identifier.serialize_json(
                value["rest_endpoint_identifier"]
            )
        )
    if "status" in value:
        import aws_sdk_apigatewayv2.types.status

        out["status"] = aws_sdk_apigatewayv2.types.status.serialize_json(
            value["status"]
        )
    if "status_exception" in value:
        import aws_sdk_apigatewayv2.types.status_exception

        out["statusException"] = (
            aws_sdk_apigatewayv2.types.status_exception.serialize_json(
                value["status_exception"]
            )
        )
    if "try_it_state" in value:
        import aws_sdk_apigatewayv2.types.try_it_state

        out["tryItState"] = aws_sdk_apigatewayv2.types.try_it_state.serialize_json(
            value["try_it_state"]
        )
    return out


def deserialize_json(data: dict) -> GetProductRestEndpointPageResponse:
    out: GetProductRestEndpointPageResponse = {}  # type: ignore[typeddict-item]
    if "displayContent" in data:
        import aws_sdk_apigatewayv2.types.endpoint_display_content_response

        out["display_content"] = (
            aws_sdk_apigatewayv2.types.endpoint_display_content_response.deserialize_json(
                data["displayContent"]
            )
        )
    if "lastModified" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastModified"]
            )
        )
    if "productRestEndpointPageArn" in data:
        out["product_rest_endpoint_page_arn"] = data["productRestEndpointPageArn"]
    if "productRestEndpointPageId" in data:
        out["product_rest_endpoint_page_id"] = data["productRestEndpointPageId"]
    if "rawDisplayContent" in data:
        out["raw_display_content"] = data["rawDisplayContent"]
    if "restEndpointIdentifier" in data:
        import aws_sdk_apigatewayv2.types.rest_endpoint_identifier

        out["rest_endpoint_identifier"] = (
            aws_sdk_apigatewayv2.types.rest_endpoint_identifier.deserialize_json(
                data["restEndpointIdentifier"]
            )
        )
    if "status" in data:
        import aws_sdk_apigatewayv2.types.status

        out["status"] = aws_sdk_apigatewayv2.types.status.deserialize_json(
            data["status"]
        )
    if "statusException" in data:
        import aws_sdk_apigatewayv2.types.status_exception

        out["status_exception"] = (
            aws_sdk_apigatewayv2.types.status_exception.deserialize_json(
                data["statusException"]
            )
        )
    if "tryItState" in data:
        import aws_sdk_apigatewayv2.types.try_it_state

        out["try_it_state"] = aws_sdk_apigatewayv2.types.try_it_state.deserialize_json(
            data["tryItState"]
        )
    return out
