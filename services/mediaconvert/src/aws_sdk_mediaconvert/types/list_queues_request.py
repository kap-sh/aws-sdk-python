"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListQueuesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max20
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.order
    import aws_sdk_mediaconvert.types.queue_list_by


class ListQueuesRequest(TypedDict):
    list_by: NotRequired["aws_sdk_mediaconvert.types.queue_list_by.QueueListBy"]
    """Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by creation date."""
    max_results: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Optional. Number of queues, up to twenty, that will be returned at one time."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use this string, provided with the response to a previous request, to request the next batch of queues."""
    order: NotRequired["aws_sdk_mediaconvert.types.order.Order"]
    """Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueuesRequest:
    out: ListQueuesRequest = {}  # type: ignore[typeddict-item]
    return out
