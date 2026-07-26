"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_event


class GetDataIntegrationEventResponse(TypedDict, closed=True):
    event: "capo_supplychain.types.data_integration_event.DataIntegrationEvent"
    """<p>The details of the DataIntegrationEvent returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationEventResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_event

    out["event"] = capo_supplychain.types.data_integration_event.serialize_json(
        value["event"]
    )
    return out


def deserialize_json(data: dict) -> GetDataIntegrationEventResponse:
    out: GetDataIntegrationEventResponse = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import capo_supplychain.types.data_integration_event

        out["event"] = capo_supplychain.types.data_integration_event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("GetDataIntegrationEventResponse.event required")
    return out
