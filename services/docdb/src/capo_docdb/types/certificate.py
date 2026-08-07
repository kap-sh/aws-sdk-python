"""Generated from Smithy shape ``com.amazonaws.docdb#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string
    import capo_docdb.types.t_stamp


class Certificate(TypedDict, closed=True):
    certificate_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The unique key that identifies a certificate.</p> <p>Example: <code>rds-ca-2019</code> </p>"""
    certificate_type: NotRequired["capo_docdb.types.string.String"]
    """<p>The type of the certificate.</p> <p>Example: <code>CA</code> </p>"""
    thumbprint: NotRequired["capo_docdb.types.string.String"]
    """<p>The thumbprint of the certificate.</p>"""
    valid_from: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p>The starting date-time from which the certificate is valid.</p> <p>Example: <code>2019-07-31T17:57:09Z</code> </p>"""
    valid_till: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p>The date-time after which the certificate is no longer valid.</p> <p>Example: <code>2024-07-31T17:57:09Z</code> </p>"""
    certificate_arn: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the certificate.</p> <p>Example: <code>arn:aws:rds:us-east-1::cert:rds-ca-2019</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Certificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "certificate_identifier" in value:
        pairs.append(
            (f"{key_prefix}CertificateIdentifier", str(value["certificate_identifier"]))
        )
    if "certificate_type" in value:
        pairs.append((f"{key_prefix}CertificateType", str(value["certificate_type"])))
    if "thumbprint" in value:
        pairs.append((f"{key_prefix}Thumbprint", str(value["thumbprint"])))
    if "valid_from" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["valid_from"], pairs, f"{key_prefix}ValidFrom"
        )
    if "valid_till" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["valid_till"], pairs, f"{key_prefix}ValidTill"
        )
    if "certificate_arn" in value:
        pairs.append((f"{key_prefix}CertificateArn", str(value["certificate_arn"])))


def deserialize_query(el: Element) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    child_certificate_identifier = el.find("CertificateIdentifier")
    if child_certificate_identifier is not None:
        out["certificate_identifier"] = str(child_certificate_identifier.text or "")
    child_certificate_type = el.find("CertificateType")
    if child_certificate_type is not None:
        out["certificate_type"] = str(child_certificate_type.text or "")
    child_thumbprint = el.find("Thumbprint")
    if child_thumbprint is not None:
        out["thumbprint"] = str(child_thumbprint.text or "")
    child_valid_from = el.find("ValidFrom")
    if child_valid_from is not None:
        import capo_docdb.types.t_stamp

        out["valid_from"] = capo_docdb.types.t_stamp.deserialize_query(child_valid_from)
    child_valid_till = el.find("ValidTill")
    if child_valid_till is not None:
        import capo_docdb.types.t_stamp

        out["valid_till"] = capo_docdb.types.t_stamp.deserialize_query(child_valid_till)
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    return out
