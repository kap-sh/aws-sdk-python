"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.certificate_authority_body
    import capo_workspaces_web.types.certificate_principal
    import capo_workspaces_web.types.certificate_thumbprint
    import capo_workspaces_web.types.timestamp


class Certificate(TypedDict, closed=True):
    thumbprint: NotRequired[
        "capo_workspaces_web.types.certificate_thumbprint.CertificateThumbprint"
    ]
    """<p>A hexadecimal identifier for the certificate.</p>"""
    subject: NotRequired[
        "capo_workspaces_web.types.certificate_principal.CertificatePrincipal"
    ]
    """<p>The entity the certificate belongs to.</p>"""
    issuer: NotRequired[
        "capo_workspaces_web.types.certificate_principal.CertificatePrincipal"
    ]
    """<p>The entity that issued the certificate.</p>"""
    not_valid_before: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The certificate is not valid before this date.</p>"""
    not_valid_after: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The certificate is not valid after this date.</p>"""
    body: NotRequired[
        "capo_workspaces_web.types.certificate_authority_body.CertificateAuthorityBody"
    ]
    """<p>The body of the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Certificate) -> dict:
    out: dict = {}
    if "thumbprint" in value:
        out["thumbprint"] = value["thumbprint"]
    if "subject" in value:
        out["subject"] = value["subject"]
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "not_valid_before" in value:
        import capo_workspaces_web.types.timestamp

        out["notValidBefore"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["not_valid_before"]
        )
    if "not_valid_after" in value:
        import capo_workspaces_web.types.timestamp

        out["notValidAfter"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["not_valid_after"]
        )
    if "body" in value:
        import capo_workspaces_web.types.certificate_authority_body

        out["body"] = (
            capo_workspaces_web.types.certificate_authority_body.serialize_json(
                value["body"]
            )
        )
    return out


def deserialize_json(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "thumbprint" in data:
        out["thumbprint"] = data["thumbprint"]
    if "subject" in data:
        out["subject"] = data["subject"]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    if "notValidBefore" in data:
        import capo_workspaces_web.types.timestamp

        out["not_valid_before"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["notValidBefore"]
        )
    if "notValidAfter" in data:
        import capo_workspaces_web.types.timestamp

        out["not_valid_after"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["notValidAfter"]
        )
    if "body" in data:
        import capo_workspaces_web.types.certificate_authority_body

        out["body"] = (
            capo_workspaces_web.types.certificate_authority_body.deserialize_json(
                data["body"]
            )
        )
    return out
