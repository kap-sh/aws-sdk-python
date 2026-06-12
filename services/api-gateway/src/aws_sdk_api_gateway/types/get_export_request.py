"""Generated from Smithy shape ``com.amazonaws.apigateway#GetExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class GetExportRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the Stage that will be exported.</p>"""
    export_type: "aws_sdk_api_gateway.types.string.String"
    """<p>The type of export. Acceptable values are 'oas30' for OpenAPI 3.0.x and 'swagger' for Swagger/OpenAPI 2.0.</p>"""
    parameters: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map of query string parameters that specify properties of the export, depending on the requested <code>exportType</code>. For <code>exportType</code> <code>oas30</code> and <code>swagger</code>, any combination of the following parameters are supported: <code>extensions='integrations'</code> or <code>extensions='apigateway'</code> will export the API with x-amazon-apigateway-integration extensions. <code>extensions='authorizers'</code> will export the API with x-amazon-apigateway-authorizer extensions. <code>postman</code> will export the API with Postman extensions, allowing for import to the Postman tool</p>"""
    accepts: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The content-type of the export, for example <code>application/json</code>. Currently <code>application/json</code> and <code>application/yaml</code> are supported for <code>exportType</code> of<code>oas30</code> and <code>swagger</code>. This should be specified in the <code>Accept</code> header for direct API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExportRequest:
    out: GetExportRequest = {}  # type: ignore[typeddict-item]
    return out
