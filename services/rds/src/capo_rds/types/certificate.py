"""Generated from Smithy shape ``com.amazonaws.rds#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class Certificate(TypedDict, closed=True):
    certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The unique key that identifies a certificate.</p>"""
    certificate_type: NotRequired["capo_rds.types.string.String"]
    """<p>The type of the certificate.</p>"""
    thumbprint: NotRequired["capo_rds.types.string.String"]
    """<p>The thumbprint of the certificate.</p>"""
    valid_from: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The starting date from which the certificate is valid.</p>"""
    valid_till: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The final date that the certificate continues to be valid.</p>"""
    certificate_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the certificate.</p>"""
    customer_override: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether there is an override for the default certificate identifier.</p>"""
    customer_override_valid_till: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>If there is an override for the default certificate identifier, when the override expires.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Certificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate_identifier" in value:
        pairs.append(
            (f"{prefix}.CertificateIdentifier", str(value["certificate_identifier"]))
        )
    if "certificate_type" in value:
        pairs.append((f"{prefix}.CertificateType", str(value["certificate_type"])))
    if "thumbprint" in value:
        pairs.append((f"{prefix}.Thumbprint", str(value["thumbprint"])))
    if "valid_from" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["valid_from"], pairs, f"{prefix}.ValidFrom"
        )
    if "valid_till" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["valid_till"], pairs, f"{prefix}.ValidTill"
        )
    if "certificate_arn" in value:
        pairs.append((f"{prefix}.CertificateArn", str(value["certificate_arn"])))
    if "customer_override" in value:
        pairs.append(
            (
                f"{prefix}.CustomerOverride",
                "true" if value["customer_override"] else "false",
            )
        )
    if "customer_override_valid_till" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["customer_override_valid_till"],
            pairs,
            f"{prefix}.CustomerOverrideValidTill",
        )


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
        import capo_rds.types.t_stamp

        out["valid_from"] = capo_rds.types.t_stamp.deserialize_query(child_valid_from)
    child_valid_till = el.find("ValidTill")
    if child_valid_till is not None:
        import capo_rds.types.t_stamp

        out["valid_till"] = capo_rds.types.t_stamp.deserialize_query(child_valid_till)
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_customer_override = el.find("CustomerOverride")
    if child_customer_override is not None:
        out["customer_override"] = (
            child_customer_override.text or ""
        ).lower() == "true"
    child_customer_override_valid_till = el.find("CustomerOverrideValidTill")
    if child_customer_override_valid_till is not None:
        import capo_rds.types.t_stamp

        out["customer_override_valid_till"] = capo_rds.types.t_stamp.deserialize_query(
            child_customer_override_valid_till
        )
    return out
