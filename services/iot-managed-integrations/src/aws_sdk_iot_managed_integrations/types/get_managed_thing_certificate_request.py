"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingCertificateRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The identifier of the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedThingCertificateRequest:
    out: GetManagedThingCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
