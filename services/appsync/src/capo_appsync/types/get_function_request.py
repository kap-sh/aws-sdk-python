"""Generated from Smithy shape ``com.amazonaws.appsync#GetFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string


class GetFunctionRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The GraphQL API ID.</p>"""
    function_id: "capo_appsync.types.resource_name.ResourceName"
    """<p>The <code>Function</code> ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFunctionRequest:
    out: GetFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
