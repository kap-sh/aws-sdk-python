"""Generated from Smithy shape ``com.amazonaws.appsync#GetIntrospectionSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.boolean_value
    import aws_sdk_appsync.types.output_type
    import aws_sdk_appsync.types.string


class GetIntrospectionSchemaRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    format: "aws_sdk_appsync.types.output_type.OutputType"
    """<p>The schema format: SDL or JSON.</p>"""
    include_directives: NotRequired["aws_sdk_appsync.types.boolean_value.BooleanValue"]
    """<p>A flag that specifies whether the schema introspection should contain directives.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntrospectionSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntrospectionSchemaRequest:
    out: GetIntrospectionSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
