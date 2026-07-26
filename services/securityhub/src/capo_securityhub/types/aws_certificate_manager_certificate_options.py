"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCertificateManagerCertificateOptions(TypedDict, closed=True):
    certificate_transparency_logging_preference: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Whether to add the certificate to a transparency log.</p> <p>Valid values: <code>DISABLED</code> | <code>ENABLED</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateOptions) -> dict:
    out: dict = {}
    if "certificate_transparency_logging_preference" in value:
        out["CertificateTransparencyLoggingPreference"] = value[
            "certificate_transparency_logging_preference"
        ]
    return out


def deserialize_json(data: dict) -> AwsCertificateManagerCertificateOptions:
    out: AwsCertificateManagerCertificateOptions = {}  # type: ignore[typeddict-item]
    if "CertificateTransparencyLoggingPreference" in data:
        out["certificate_transparency_logging_preference"] = data[
            "CertificateTransparencyLoggingPreference"
        ]
    return out
