"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string


class DeleteDataSourceRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The name of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSourceRequest:
    out: DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
