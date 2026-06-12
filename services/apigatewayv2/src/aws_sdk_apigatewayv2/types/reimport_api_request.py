"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ReimportApiRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__string


class ReimportApiRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    basepath: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.</p>"""
    body: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The OpenAPI definition. Supported only for HTTP APIs.</p>"""
    fail_on_warnings: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReimportApiRequest) -> dict:
    out: dict = {}
    if "body" in value:
        out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> ReimportApiRequest:
    out: ReimportApiRequest = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    return out
