"""Generated from Smithy shape ``com.amazonaws.licensemanager#IssuerDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class IssuerDetails(TypedDict):
    name: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Issuer name.</p>"""
    sign_key: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Asymmetric KMS key from Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.</p>"""
    key_fingerprint: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Issuer key fingerprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssuerDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "sign_key" in value:
        out["SignKey"] = value["sign_key"]
    if "key_fingerprint" in value:
        out["KeyFingerprint"] = value["key_fingerprint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IssuerDetails:
    out: IssuerDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SignKey" in data:
        out["sign_key"] = data["SignKey"]
    if "KeyFingerprint" in data:
        out["key_fingerprint"] = data["KeyFingerprint"]
    return out
