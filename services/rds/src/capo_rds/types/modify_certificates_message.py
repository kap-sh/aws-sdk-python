"""Generated from Smithy shape ``com.amazonaws.rds#ModifyCertificatesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.string


class ModifyCertificatesMessage(TypedDict, closed=True):
    certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The new default certificate identifier to override the current one with.</p> <p>To determine the valid values, use the <code>describe-certificates</code> CLI command or the <code>DescribeCertificates</code> API operation.</p>"""
    remove_customer_override: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to remove the override for the default certificate. If the override is removed, the default certificate is the system default.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCertificatesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate_identifier" in value:
        pairs.append(
            (f"{prefix}.CertificateIdentifier", str(value["certificate_identifier"]))
        )
    if "remove_customer_override" in value:
        pairs.append(
            (
                f"{prefix}.RemoveCustomerOverride",
                "true" if value["remove_customer_override"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyCertificatesMessage:
    out: ModifyCertificatesMessage = {}  # type: ignore[typeddict-item]
    child_certificate_identifier = el.find("CertificateIdentifier")
    if child_certificate_identifier is not None:
        out["certificate_identifier"] = str(child_certificate_identifier.text or "")
    child_remove_customer_override = el.find("RemoveCustomerOverride")
    if child_remove_customer_override is not None:
        out["remove_customer_override"] = (
            child_remove_customer_override.text or ""
        ).lower() == "true"
    return out
