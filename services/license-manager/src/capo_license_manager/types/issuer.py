"""Generated from Smithy shape ``com.amazonaws.licensemanager#Issuer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.string


class Issuer(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>Issuer name.</p>"""
    sign_key: NotRequired["capo_license_manager.types.string.String"]
    """<p>Asymmetric KMS key from Key Management Service. The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Issuer) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "sign_key" in value:
        out["SignKey"] = value["sign_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Issuer:
    out: Issuer = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Issuer.name required")
    if "SignKey" in data:
        out["sign_key"] = data["SignKey"]
    return out
