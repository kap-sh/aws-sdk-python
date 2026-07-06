"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.certificate_pem
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingCertificateResponse(TypedDict, closed=True):
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The identifier of the managed thing.</p>"""
    certificate_pem: NotRequired[
        "aws_sdk_iot_managed_integrations.types.certificate_pem.CertificatePem"
    ]
    """<p>The PEM-encoded certificate for the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingCertificateResponse) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "certificate_pem" in value:
        out["CertificatePem"] = value["certificate_pem"]
    return out


def deserialize_json(data: dict) -> GetManagedThingCertificateResponse:
    out: GetManagedThingCertificateResponse = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "CertificatePem" in data:
        out["certificate_pem"] = data["CertificatePem"]
    return out
