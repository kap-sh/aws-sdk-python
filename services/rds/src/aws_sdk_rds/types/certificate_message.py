"""Generated from Smithy shape ``com.amazonaws.rds#CertificateMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.certificate_list
    import aws_sdk_rds.types.string


class CertificateMessage(TypedDict):
    default_certificate_for_new_launches: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The default root CA for new databases created by your Amazon Web Services account. This is either the root CA override set on your Amazon Web Services account or the system default CA for the Region if no override exists. To override the default CA, use the <code>ModifyCertificates</code> operation.</p>"""
    certificates: NotRequired["aws_sdk_rds.types.certificate_list.CertificateList"]
    """<p>The list of <code>Certificate</code> objects for the Amazon Web Services account.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeCertificates</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "default_certificate_for_new_launches" in value:
        pairs.append(
            (
                f"{prefix}.DefaultCertificateForNewLaunches",
                str(value["default_certificate_for_new_launches"]),
            )
        )
    if "certificates" in value:
        import aws_sdk_rds.types.certificate_list

        aws_sdk_rds.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{prefix}.Certificates"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> CertificateMessage:
    out: CertificateMessage = {}  # type: ignore[typeddict-item]
    child_default_certificate_for_new_launches = el.find(
        "DefaultCertificateForNewLaunches"
    )
    if child_default_certificate_for_new_launches is not None:
        out["default_certificate_for_new_launches"] = str(
            child_default_certificate_for_new_launches.text or ""
        )
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import aws_sdk_rds.types.certificate_list

        out["certificates"] = aws_sdk_rds.types.certificate_list.deserialize_query(
            child_certificates
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
