"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ExportApiRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__string


class ExportApiRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    export_version: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is 1.0.</p>"""
    include_extensions: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    r"""<p>Specifies whether to include <a href=\"https://docs.aws.amazon.com//apigateway/latest/developerguide/api-gateway-swagger-extensions.html\">API Gateway extensions</a> in the exported API definition. API Gateway extensions are included by default.</p>"""
    output_type: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The output type of the exported definition file. Valid values are JSON and YAML.</p>"""
    specification: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value.</p>"""
    stage_name: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportApiRequest:
    out: ExportApiRequest = {}  # type: ignore[typeddict-item]
    return out
