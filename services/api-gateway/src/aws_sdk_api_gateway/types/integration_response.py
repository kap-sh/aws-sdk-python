"""Generated from Smithy shape ``com.amazonaws.apigateway#IntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.content_handling_strategy
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.status_code
    import aws_sdk_api_gateway.types.string


class IntegrationResponse(TypedDict, closed=True):
    status_code: NotRequired["aws_sdk_api_gateway.types.status_code.StatusCode"]
    """<p>Specifies the status code that is used to map the integration response to an existing MethodResponse.</p>"""
    selection_pattern: NotRequired["aws_sdk_api_gateway.types.string.String"]
    r"""<p>Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error response returns some string, you could use the <code>.+</code> regex to match error response. However, make sure that the error response does not contain any newline (<code>\n</code>) character in such cases. If the back end is an Lambda function, the Lambda function error header is matched. For all other HTTP and Amazon Web Services back ends, the HTTP status code is matched.</p>"""
    response_parameters: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of <code>method.response.header.{name}</code>, where <code>name</code> is a valid and unique header name. The mapped non-static value must match the pattern of <code>integration.response.header.{name}</code> or <code>integration.response.body.{JSON-expression}</code>, where <code>name</code> is a valid and unique response header name and <code>JSON-expression</code> is a valid JSON expression without the <code>$</code> prefix.</p>"""
    response_templates: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>"""
    content_handling: NotRequired[
        "aws_sdk_api_gateway.types.content_handling_strategy.ContentHandlingStrategy"
    ]
    """<p>Specifies how to handle response payload content type conversions. Supported values are <code>CONVERT_TO_BINARY</code> and <code>CONVERT_TO_TEXT</code>, with the following behaviors:</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationResponse) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "selection_pattern" in value:
        out["selectionPattern"] = value["selection_pattern"]
    if "response_parameters" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["responseParameters"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["response_parameters"]
            )
        )
    if "response_templates" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["responseTemplates"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["response_templates"]
            )
        )
    if "content_handling" in value:
        import aws_sdk_api_gateway.types.content_handling_strategy

        out["contentHandling"] = (
            aws_sdk_api_gateway.types.content_handling_strategy.serialize_json(
                value["content_handling"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegrationResponse:
    out: IntegrationResponse = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "selectionPattern" in data:
        out["selection_pattern"] = data["selectionPattern"]
    if "responseParameters" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["response_parameters"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["responseParameters"]
            )
        )
    if "responseTemplates" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["response_templates"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["responseTemplates"]
            )
        )
    if "contentHandling" in data:
        import aws_sdk_api_gateway.types.content_handling_strategy

        out["content_handling"] = (
            aws_sdk_api_gateway.types.content_handling_strategy.deserialize_json(
                data["contentHandling"]
            )
        )
    return out
