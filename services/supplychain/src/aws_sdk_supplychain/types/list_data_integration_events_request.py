"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_event_max_results
    import aws_sdk_supplychain.types.data_integration_event_next_token
    import aws_sdk_supplychain.types.data_integration_event_type
    import aws_sdk_supplychain.types.uuid


class ListDataIntegrationEventsRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    event_type: NotRequired[
        "aws_sdk_supplychain.types.data_integration_event_type.DataIntegrationEventType"
    ]
    """<p>List data integration events for the specified eventType.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
    ]
    """<p>The pagination token to fetch the next page of the data integration events.</p>"""
    max_results: "aws_sdk_supplychain.types.data_integration_event_max_results.DataIntegrationEventMaxResults"
    """<p>Specify the maximum number of data integration events to fetch in one paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationEventsRequest:
    out: ListDataIntegrationEventsRequest = {}  # type: ignore[typeddict-item]
    return out
