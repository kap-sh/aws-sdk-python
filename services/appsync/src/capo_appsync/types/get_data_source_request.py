"""Generated from Smithy shape ``com.amazonaws.appsync#GetDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string


class GetDataSourceRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The name of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSourceRequest:
    out: GetDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
