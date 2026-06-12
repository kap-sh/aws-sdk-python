"""Generated from Smithy shape ``com.amazonaws.appsync#GetDataSourceIntrospectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.boolean
    import aws_sdk_appsync.types.max_results
    import aws_sdk_appsync.types.pagination_token
    import aws_sdk_appsync.types.string


class GetDataSourceIntrospectionRequest(TypedDict):
    introspection_id: "aws_sdk_appsync.types.string.String"
    """<p>The introspection ID. Each introspection contains a unique ID that can be used to reference the instrospection record.</p>"""
    include_models_sdl: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>A boolean flag that determines whether SDL should be generated for introspected types. If set to <code>true</code>, each model will contain an <code>sdl</code> property that contains the SDL for that type. The SDL only contains the type data and no additional metadata or directives. </p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>Determines the number of types to be returned in a single response before paginating. This value is typically taken from <code>nextToken</code> value from the previous response.</p>"""
    max_results: "aws_sdk_appsync.types.max_results.MaxResults"
    """<p>The maximum number of introspected types that will be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceIntrospectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceIntrospectionRequest:
    out: GetDataSourceIntrospectionRequest = {}  # type: ignore[typeddict-item]
    return out
