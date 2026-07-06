"""Generated from Smithy shape ``com.amazonaws.docdb#CertificateMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.certificate_list
    import aws_sdk_docdb.types.string


class CertificateMessage(TypedDict, closed=True):
    certificates: NotRequired["aws_sdk_docdb.types.certificate_list.CertificateList"]
    """<p>A list of certificates for this Amazon Web Services account.</p>"""
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided if the number of records retrieved is greater than <code>MaxRecords</code>. If this parameter is specified, the marker specifies the next record in the list. Including the value of <code>Marker</code> in the next call to <code>DescribeCertificates</code> results in the next page of certificates.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificates" in value:
        import aws_sdk_docdb.types.certificate_list

        aws_sdk_docdb.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{prefix}.Certificates"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> CertificateMessage:
    out: CertificateMessage = {}  # type: ignore[typeddict-item]
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import aws_sdk_docdb.types.certificate_list

        out["certificates"] = aws_sdk_docdb.types.certificate_list.deserialize_query(
            child_certificates
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
