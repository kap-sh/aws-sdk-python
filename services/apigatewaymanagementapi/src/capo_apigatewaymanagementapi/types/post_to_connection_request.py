"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#PostToConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewaymanagementapi.types.__string
    import capo_apigatewaymanagementapi.types.data


class PostToConnectionRequest(TypedDict, closed=True):
    data: NotRequired["capo_apigatewaymanagementapi.types.data.Data"]
    """<p>The data to be sent to the client specified by its connection id.</p>"""
    connection_id: "capo_apigatewaymanagementapi.types.__string.__string"
    """<p>The identifier of the connection that a specific client is using.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostToConnectionRequest) -> dict:
    out: dict = {}
    if "data" in value:
        import capo_apigatewaymanagementapi.types.data

        out["Data"] = capo_apigatewaymanagementapi.types.data.serialize_json(
            value["data"]
        )
    return out


def deserialize_json(data: dict) -> PostToConnectionRequest:
    out: PostToConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import capo_apigatewaymanagementapi.types.data

        out["data"] = capo_apigatewaymanagementapi.types.data.deserialize_json(
            data["Data"]
        )
    return out
