"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateExtendedKeyUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCertificateManagerCertificateExtendedKeyUsage(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of an extension value. Indicates the purpose for which the certificate public key can be used.</p>"""
    o_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An object identifier (OID) for the extension value.</p> <p>The format is numbers separated by periods.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateExtendedKeyUsage) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "o_id" in value:
        out["OId"] = value["o_id"]
    return out


def deserialize_json(data: dict) -> AwsCertificateManagerCertificateExtendedKeyUsage:
    out: AwsCertificateManagerCertificateExtendedKeyUsage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OId" in data:
        out["o_id"] = data["OId"]
    return out
