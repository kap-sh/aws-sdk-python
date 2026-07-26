"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateProvisioningProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.claim_certificate
    import capo_iot_managed_integrations.types.claim_certificate_private_key
    import capo_iot_managed_integrations.types.provisioning_profile_arn
    import capo_iot_managed_integrations.types.provisioning_profile_id
    import capo_iot_managed_integrations.types.provisioning_profile_name
    import capo_iot_managed_integrations.types.provisioning_profile_status
    import capo_iot_managed_integrations.types.provisioning_type


class CreateProvisioningProfileResponse(TypedDict, closed=True):
    arn: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_arn.ProvisioningProfileArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the provisioning profile.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
    ]
    """<p>The name of the provisioning profile.</p>"""
    provisioning_type: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType"
    ]
    """<p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>"""
    id: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId"
    ]
    """<p>The identifier of the provisioning profile.</p>"""
    status: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_status.ProvisioningProfileStatus"
    ]
    """<p>The status of a provisioning profile.</p>"""
    claim_certificate: NotRequired[
        "capo_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
    ]
    """<p>The body of the PEM-encoded claim certificate.</p>"""
    claim_certificate_private_key: NotRequired[
        "capo_iot_managed_integrations.types.claim_certificate_private_key.ClaimCertificatePrivateKey"
    ]
    """<p>The private key of the claim certificate. This may be stored securely on the device for validating the connection endpoint with IoT managed integrations using the public key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "provisioning_type" in value:
        import capo_iot_managed_integrations.types.provisioning_type

        out["ProvisioningType"] = (
            capo_iot_managed_integrations.types.provisioning_type.serialize_json(
                value["provisioning_type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_iot_managed_integrations.types.provisioning_profile_status

        out["Status"] = (
            capo_iot_managed_integrations.types.provisioning_profile_status.serialize_json(
                value["status"]
            )
        )
    if "claim_certificate" in value:
        out["ClaimCertificate"] = value["claim_certificate"]
    if "claim_certificate_private_key" in value:
        out["ClaimCertificatePrivateKey"] = value["claim_certificate_private_key"]
    return out


def deserialize_json(data: dict) -> CreateProvisioningProfileResponse:
    out: CreateProvisioningProfileResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ProvisioningType" in data:
        import capo_iot_managed_integrations.types.provisioning_type

        out["provisioning_type"] = (
            capo_iot_managed_integrations.types.provisioning_type.deserialize_json(
                data["ProvisioningType"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Status" in data:
        import capo_iot_managed_integrations.types.provisioning_profile_status

        out["status"] = (
            capo_iot_managed_integrations.types.provisioning_profile_status.deserialize_json(
                data["Status"]
            )
        )
    if "ClaimCertificate" in data:
        out["claim_certificate"] = data["ClaimCertificate"]
    if "ClaimCertificatePrivateKey" in data:
        out["claim_certificate_private_key"] = data["ClaimCertificatePrivateKey"]
    return out
