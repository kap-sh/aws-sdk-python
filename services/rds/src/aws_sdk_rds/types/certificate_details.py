"""Generated from Smithy shape ``com.amazonaws.rds#CertificateDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.t_stamp


class CertificateDetails(TypedDict):
    ca_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The CA identifier of the CA certificate used for the DB instance's server certificate.</p>"""
    valid_till: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The expiration date of the DB instance’s server certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ca_identifier" in value:
        pairs.append((f"{prefix}.CAIdentifier", str(value["ca_identifier"])))
    if "valid_till" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["valid_till"], pairs, f"{prefix}.ValidTill"
        )


def deserialize_query(el: Element) -> CertificateDetails:
    out: CertificateDetails = {}  # type: ignore[typeddict-item]
    child_ca_identifier = el.find("CAIdentifier")
    if child_ca_identifier is not None:
        out["ca_identifier"] = str(child_ca_identifier.text or "")
    child_valid_till = el.find("ValidTill")
    if child_valid_till is not None:
        import aws_sdk_rds.types.t_stamp

        out["valid_till"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_valid_till
        )
    return out
