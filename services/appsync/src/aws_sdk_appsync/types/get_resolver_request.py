"""Generated from Smithy shape ``com.amazonaws.appsync#GetResolverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string


class GetResolverRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The resolver type name.</p>"""
    field_name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The resolver field name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResolverRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResolverRequest:
    out: GetResolverRequest = {}  # type: ignore[typeddict-item]
    return out
