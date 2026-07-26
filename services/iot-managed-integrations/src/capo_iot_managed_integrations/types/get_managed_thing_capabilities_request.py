"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingCapabilitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.managed_thing_id


class GetManagedThingCapabilitiesRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The id of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingCapabilitiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingCapabilitiesRequest:
    out: GetManagedThingCapabilitiesRequest = {}  # type: ignore[typeddict-item]
    return out
