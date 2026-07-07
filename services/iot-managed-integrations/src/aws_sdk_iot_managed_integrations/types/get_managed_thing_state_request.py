"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingStateRequest(TypedDict, closed=True):
    managed_thing_id: (
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The id of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingStateRequest:
    out: GetManagedThingStateRequest = {}  # type: ignore[typeddict-item]
    return out
