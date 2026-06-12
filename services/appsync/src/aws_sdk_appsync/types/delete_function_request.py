"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string


class DeleteFunctionRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The GraphQL API ID.</p>"""
    function_id: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The <code>Function</code> ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionRequest:
    out: DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
