"""Generated from Smithy shape ``com.amazonaws.odb#OciIdentityDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class OciIdentityDomain(TypedDict, closed=True):
    oci_identity_domain_id: NotRequired["str"]
    """<p>The unique identifier of the OCI identity domain.</p>"""
    oci_identity_domain_resource_url: NotRequired["str"]
    """<p>The resource URL for accessing the OCI identity domain.</p>"""
    oci_identity_domain_url: NotRequired["str"]
    """<p>The URL of the OCI identity domain.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the OCI identity domain.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the OCI identity domain, if applicable.</p>"""
    account_setup_cloud_formation_url: NotRequired["str"]
    """<p>The Amazon Web Services CloudFormation URL for setting up the account integration with the OCI identity domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciIdentityDomain) -> dict:
    out: dict = {}
    if "oci_identity_domain_id" in value:
        out["ociIdentityDomainId"] = value["oci_identity_domain_id"]
    if "oci_identity_domain_resource_url" in value:
        out["ociIdentityDomainResourceUrl"] = value["oci_identity_domain_resource_url"]
    if "oci_identity_domain_url" in value:
        out["ociIdentityDomainUrl"] = value["oci_identity_domain_url"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "account_setup_cloud_formation_url" in value:
        out["accountSetupCloudFormationUrl"] = value[
            "account_setup_cloud_formation_url"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> OciIdentityDomain:
    out: OciIdentityDomain = {}  # type: ignore[typeddict-item]
    if "ociIdentityDomainId" in data:
        out["oci_identity_domain_id"] = data["ociIdentityDomainId"]
    if "ociIdentityDomainResourceUrl" in data:
        out["oci_identity_domain_resource_url"] = data["ociIdentityDomainResourceUrl"]
    if "ociIdentityDomainUrl" in data:
        out["oci_identity_domain_url"] = data["ociIdentityDomainUrl"]
    if "status" in data:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "accountSetupCloudFormationUrl" in data:
        out["account_setup_cloud_formation_url"] = data["accountSetupCloudFormationUrl"]
    return out
