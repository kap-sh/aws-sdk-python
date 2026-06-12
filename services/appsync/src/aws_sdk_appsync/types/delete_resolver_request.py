"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteResolverRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string


class DeleteResolverRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The name of the resolver type.</p>"""
    field_name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The resolver field name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResolverRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResolverRequest:
    out: DeleteResolverRequest = {}  # type: ignore[typeddict-item]
    return out
