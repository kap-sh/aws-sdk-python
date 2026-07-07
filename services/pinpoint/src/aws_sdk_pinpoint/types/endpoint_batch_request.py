"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_of_endpoint_batch_item


class EndpointBatchRequest(TypedDict, closed=True):
    item: NotRequired[
        "aws_sdk_pinpoint.types.list_of_endpoint_batch_item.ListOfEndpointBatchItem"
    ]
    """<p>An array that defines the endpoints to create or update and, for each endpoint, the property values to set or change. An array can contain a maximum of 100 items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointBatchRequest) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_pinpoint.types.list_of_endpoint_batch_item

        out["Item"] = aws_sdk_pinpoint.types.list_of_endpoint_batch_item.serialize_json(
            value["item"]
        )
    return out


def deserialize_json(data: dict) -> EndpointBatchRequest:
    out: EndpointBatchRequest = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_pinpoint.types.list_of_endpoint_batch_item

        out["item"] = (
            aws_sdk_pinpoint.types.list_of_endpoint_batch_item.deserialize_json(
                data["Item"]
            )
        )
    return out
