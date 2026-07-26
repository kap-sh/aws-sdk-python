"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string


class DeleteTypeRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The type name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTypeRequest:
    out: DeleteTypeRequest = {}  # type: ignore[typeddict-item]
    return out
