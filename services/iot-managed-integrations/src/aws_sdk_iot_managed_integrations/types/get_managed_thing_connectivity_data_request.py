"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingConnectivityDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingConnectivityDataRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The identifier of a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingConnectivityDataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingConnectivityDataRequest:
    out: GetManagedThingConnectivityDataRequest = {}  # type: ignore[typeddict-item]
    return out
