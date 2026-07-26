"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateKeyUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCertificateManagerCertificateKeyUsage(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The key usage extension name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateKeyUsage) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AwsCertificateManagerCertificateKeyUsage:
    out: AwsCertificateManagerCertificateKeyUsage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
