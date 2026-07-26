"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string


class DeleteFunctionRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The GraphQL API ID.</p>"""
    function_id: "capo_appsync.types.resource_name.ResourceName"
    """<p>The <code>Function</code> ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFunctionRequest:
    out: DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
