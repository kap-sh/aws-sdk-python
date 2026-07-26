"""Generated from Smithy shape ``com.amazonaws.odb#InitializeServiceInput``."""

from typing_extensions import TypedDict


class InitializeServiceInput(TypedDict, closed=True):
    oci_identity_domain: "bool"
    """<p>The Oracle Cloud Infrastructure (OCI) identity domain configuration for service initialization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InitializeServiceInput) -> dict:
    out: dict = {}
    out["ociIdentityDomain"] = value.get("oci_identity_domain", True)
    return out


def deserialize_aws_json_1_0(data: dict) -> InitializeServiceInput:
    out: InitializeServiceInput = {}  # type: ignore[typeddict-item]
    if "ociIdentityDomain" in data:
        out["oci_identity_domain"] = data["ociIdentityDomain"]
    else:
        out["oci_identity_domain"] = True
    return out
