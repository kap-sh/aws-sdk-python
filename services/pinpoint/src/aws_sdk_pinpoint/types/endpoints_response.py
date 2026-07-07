"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_of_endpoint_response


class EndpointsResponse(TypedDict, closed=True):
    item: NotRequired[
        "aws_sdk_pinpoint.types.list_of_endpoint_response.ListOfEndpointResponse"
    ]
    """<p>An array of responses, one for each endpoint that's associated with the user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointsResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_pinpoint.types.list_of_endpoint_response

        out["Item"] = aws_sdk_pinpoint.types.list_of_endpoint_response.serialize_json(
            value["item"]
        )
    return out


def deserialize_json(data: dict) -> EndpointsResponse:
    out: EndpointsResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_pinpoint.types.list_of_endpoint_response

        out["item"] = aws_sdk_pinpoint.types.list_of_endpoint_response.deserialize_json(
            data["Item"]
        )
    return out
