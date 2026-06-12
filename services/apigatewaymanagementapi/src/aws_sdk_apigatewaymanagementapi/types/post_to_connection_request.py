"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#PostToConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewaymanagementapi.types.__string
    import aws_sdk_apigatewaymanagementapi.types.data


class PostToConnectionRequest(TypedDict):
    data: NotRequired["aws_sdk_apigatewaymanagementapi.types.data.Data"]
    """<p>The data to be sent to the client specified by its connection id.</p>"""
    connection_id: "aws_sdk_apigatewaymanagementapi.types.__string.__string"
    """<p>The identifier of the connection that a specific client is using.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostToConnectionRequest) -> dict:
    out: dict = {}
    if "data" in value:
        import aws_sdk_apigatewaymanagementapi.types.data

        out["Data"] = aws_sdk_apigatewaymanagementapi.types.data.serialize_json(
            value["data"]
        )
    return out


def deserialize_json(data: dict) -> PostToConnectionRequest:
    out: PostToConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import aws_sdk_apigatewaymanagementapi.types.data

        out["data"] = aws_sdk_apigatewaymanagementapi.types.data.deserialize_json(
            data["Data"]
        )
    return out
