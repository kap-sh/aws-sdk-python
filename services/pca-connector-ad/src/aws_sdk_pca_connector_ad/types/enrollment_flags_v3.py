"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#EnrollmentFlagsV3``."""

from typing_extensions import NotRequired, TypedDict


class EnrollmentFlagsV3(TypedDict, closed=True):
    include_symmetric_algorithms: NotRequired["bool"]
    """<p>Include symmetric algorithms allowed by the subject.</p>"""
    user_interaction_required: NotRequired["bool"]
    """<p>Require user interaction when the subject is enrolled and the private key associated with the certificate is used.</p>"""
    remove_invalid_certificate_from_personal_store: NotRequired["bool"]
    """<p>Delete expired or revoked certificates instead of archiving them.</p>"""
    no_security_extension: NotRequired["bool"]
    """<p>This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.</p>"""
    enable_key_reuse_on_nt_token_keyset_storage_full: NotRequired["bool"]
    """<p>Allow renewal using the same key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnrollmentFlagsV3) -> dict:
    out: dict = {}
    if "include_symmetric_algorithms" in value:
        out["IncludeSymmetricAlgorithms"] = value["include_symmetric_algorithms"]
    if "user_interaction_required" in value:
        out["UserInteractionRequired"] = value["user_interaction_required"]
    if "remove_invalid_certificate_from_personal_store" in value:
        out["RemoveInvalidCertificateFromPersonalStore"] = value[
            "remove_invalid_certificate_from_personal_store"
        ]
    if "no_security_extension" in value:
        out["NoSecurityExtension"] = value["no_security_extension"]
    if "enable_key_reuse_on_nt_token_keyset_storage_full" in value:
        out["EnableKeyReuseOnNtTokenKeysetStorageFull"] = value[
            "enable_key_reuse_on_nt_token_keyset_storage_full"
        ]
    return out


def deserialize_json(data: dict) -> EnrollmentFlagsV3:
    out: EnrollmentFlagsV3 = {}  # type: ignore[typeddict-item]
    if "IncludeSymmetricAlgorithms" in data:
        out["include_symmetric_algorithms"] = data["IncludeSymmetricAlgorithms"]
    if "UserInteractionRequired" in data:
        out["user_interaction_required"] = data["UserInteractionRequired"]
    if "RemoveInvalidCertificateFromPersonalStore" in data:
        out["remove_invalid_certificate_from_personal_store"] = data[
            "RemoveInvalidCertificateFromPersonalStore"
        ]
    if "NoSecurityExtension" in data:
        out["no_security_extension"] = data["NoSecurityExtension"]
    if "EnableKeyReuseOnNtTokenKeysetStorageFull" in data:
        out["enable_key_reuse_on_nt_token_keyset_storage_full"] = data[
            "EnableKeyReuseOnNtTokenKeysetStorageFull"
        ]
    return out
