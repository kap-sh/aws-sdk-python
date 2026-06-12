"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The id of the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingRequest:
    out: GetManagedThingRequest = {}  # type: ignore[typeddict-item]
    return out
