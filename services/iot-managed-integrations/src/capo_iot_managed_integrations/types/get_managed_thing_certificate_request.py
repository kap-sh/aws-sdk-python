"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.managed_thing_id


class GetManagedThingCertificateRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The identifier of the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingCertificateRequest:
    out: GetManagedThingCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
