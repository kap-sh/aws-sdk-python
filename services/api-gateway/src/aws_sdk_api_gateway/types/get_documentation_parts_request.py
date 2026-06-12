"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDocumentationPartsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.documentation_part_type
    import aws_sdk_api_gateway.types.location_status_type
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetDocumentationPartsRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    type: NotRequired[
        "aws_sdk_api_gateway.types.documentation_part_type.DocumentationPartType"
    ]
    """<p>The type of API entities of the to-be-retrieved documentation parts. </p>"""
    name_query: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of API entities of the to-be-retrieved documentation parts.</p>"""
    path: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The path of API entities of the to-be-retrieved documentation parts.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""
    location_status: NotRequired[
        "aws_sdk_api_gateway.types.location_status_type.LocationStatusType"
    ]
    """<p>The status of the API documentation parts to retrieve. Valid values are <code>DOCUMENTED</code> for retrieving DocumentationPart resources with content and <code>UNDOCUMENTED</code> for DocumentationPart resources without content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentationPartsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentationPartsRequest:
    out: GetDocumentationPartsRequest = {}  # type: ignore[typeddict-item]
    return out
