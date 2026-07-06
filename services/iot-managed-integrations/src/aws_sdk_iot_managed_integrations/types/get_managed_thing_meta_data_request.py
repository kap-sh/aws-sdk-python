"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingMetaDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingMetaDataRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The managed thing id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingMetaDataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingMetaDataRequest:
    out: GetManagedThingMetaDataRequest = {}  # type: ignore[typeddict-item]
    return out
