"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachCertificateToDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class AttachCertificateToDistributionRequest(TypedDict):
    distribution_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the distribution that the certificate will be attached to.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""
    certificate_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the certificate to attach to a distribution.</p> <p>Only certificates with a status of <code>ISSUED</code> can be attached to a distribution.</p> <p>Use the <code>GetCertificates</code> action to get a list of certificate names that you can specify.</p> <note> <p>This is the name of the certificate resource type and is used only to reference the certificate in other API actions. It can be different than the domain name of the certificate. For example, your certificate name might be <code>WordPress-Blog-Certificate</code> and the domain name of the certificate might be <code>example.com</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachCertificateToDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    out["certificateName"] = value["certificate_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachCertificateToDistributionRequest:
    out: AttachCertificateToDistributionRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    else:
        raise DeserializationError(
            "AttachCertificateToDistributionRequest.distribution_name required"
        )
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    else:
        raise DeserializationError(
            "AttachCertificateToDistributionRequest.certificate_name required"
        )
    return out
