"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfEndpointBatchItem``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.endpoint_batch_item

ListOfEndpointBatchItem: TypeAlias = list[
    "capo_pinpoint.types.endpoint_batch_item.EndpointBatchItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfEndpointBatchItem) -> list:
    import capo_pinpoint.types.endpoint_batch_item

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.endpoint_batch_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfEndpointBatchItem:
    import capo_pinpoint.types.endpoint_batch_item

    out: ListOfEndpointBatchItem = []
    for item in data:
        out.append(capo_pinpoint.types.endpoint_batch_item.deserialize_json(item))
    return out
