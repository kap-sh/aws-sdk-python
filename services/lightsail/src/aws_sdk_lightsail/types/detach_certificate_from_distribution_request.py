"""Generated from Smithy shape ``com.amazonaws.lightsail#DetachCertificateFromDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DetachCertificateFromDistributionRequest(TypedDict):
    distribution_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the distribution from which to detach the certificate.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachCertificateFromDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachCertificateFromDistributionRequest:
    out: DetachCertificateFromDistributionRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    else:
        raise DeserializationError(
            "DetachCertificateFromDistributionRequest.distribution_name required"
        )
    return out
