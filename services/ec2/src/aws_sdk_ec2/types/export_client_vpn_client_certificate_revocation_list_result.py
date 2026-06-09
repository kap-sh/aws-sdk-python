"""Generated from Smithy shape ``com.amazonaws.ec2#ExportClientVpnClientCertificateRevocationListResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_certificate_revocation_list_status
    import aws_sdk_ec2.types.string


class ExportClientVpnClientCertificateRevocationListResult(TypedDict):
    certificate_revocation_list: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Information about the client certificate revocation list.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_certificate_revocation_list_status.ClientCertificateRevocationListStatus"
    ]
    """<p>The current state of the client certificate revocation list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportClientVpnClientCertificateRevocationListResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "certificate_revocation_list" in value:
        pairs.append(
            (
                f"{prefix}.CertificateRevocationList",
                str(value["certificate_revocation_list"]),
            )
        )
    if "status" in value:
        import aws_sdk_ec2.types.client_certificate_revocation_list_status

        aws_sdk_ec2.types.client_certificate_revocation_list_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(
    el: Element,
) -> ExportClientVpnClientCertificateRevocationListResult:
    out: ExportClientVpnClientCertificateRevocationListResult = {}  # type: ignore[typeddict-item]
    child_certificate_revocation_list = el.find("CertificateRevocationList")
    if child_certificate_revocation_list is not None:
        out["certificate_revocation_list"] = str(
            child_certificate_revocation_list.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.client_certificate_revocation_list_status

        out["status"] = (
            aws_sdk_ec2.types.client_certificate_revocation_list_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
