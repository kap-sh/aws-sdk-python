"""Generated from Smithy shape ``com.amazonaws.appsync#GetTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string
    import aws_sdk_appsync.types.type_definition_format


class GetTypeRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The type name.</p>"""
    format: "aws_sdk_appsync.types.type_definition_format.TypeDefinitionFormat"
    """<p>The type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTypeRequest:
    out: GetTypeRequest = {}  # type: ignore[typeddict-item]
    return out
