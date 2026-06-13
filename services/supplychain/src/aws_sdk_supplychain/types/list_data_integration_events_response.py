"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_event_list
    import aws_sdk_supplychain.types.data_integration_event_next_token


class ListDataIntegrationEventsResponse(TypedDict):
    events: (
        "aws_sdk_supplychain.types.data_integration_event_list.DataIntegrationEventList"
    )
    """<p>The list of data integration events.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
    ]
    """<p>The pagination token to fetch the next page of the ListDataIntegrationEvents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_event_list

    out["events"] = (
        aws_sdk_supplychain.types.data_integration_event_list.serialize_json(
            value["events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationEventsResponse:
    out: ListDataIntegrationEventsResponse = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_supplychain.types.data_integration_event_list

        out["events"] = (
            aws_sdk_supplychain.types.data_integration_event_list.deserialize_json(
                data["events"]
            )
        )
    else:
        raise DeserializationError("ListDataIntegrationEventsResponse.events required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
