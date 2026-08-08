"""Generated from Smithy shape ``com.amazonaws.ec2#ExportClientVpnClientCertificateRevocationListResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_certificate_revocation_list_status
    import capo_ec2.types.string


class ExportClientVpnClientCertificateRevocationListResult(TypedDict, closed=True):
    certificate_revocation_list: NotRequired["capo_ec2.types.string.String"]
    """<p>Information about the client certificate revocation list.</p>"""
    status: NotRequired[
        "capo_ec2.types.client_certificate_revocation_list_status.ClientCertificateRevocationListStatus"
    ]
    """<p>The current state of the client certificate revocation list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportClientVpnClientCertificateRevocationListResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "certificate_revocation_list" in value:
        pairs.append(
            (
                f"{key_prefix}CertificateRevocationList",
                str(value["certificate_revocation_list"]),
            )
        )
    if "status" in value:
        import capo_ec2.types.client_certificate_revocation_list_status

        capo_ec2.types.client_certificate_revocation_list_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(
    el: Element,
) -> ExportClientVpnClientCertificateRevocationListResult:
    out: ExportClientVpnClientCertificateRevocationListResult = {}  # type: ignore[typeddict-item]
    child_certificate_revocation_list = el.find("certificateRevocationList")
    if child_certificate_revocation_list is not None:
        out["certificate_revocation_list"] = str(
            child_certificate_revocation_list.text or ""
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.client_certificate_revocation_list_status

        out["status"] = (
            capo_ec2.types.client_certificate_revocation_list_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
