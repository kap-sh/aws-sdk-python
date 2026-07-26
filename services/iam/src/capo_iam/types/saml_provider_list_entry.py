"""Generated from Smithy shape ``com.amazonaws.iam#SAMLProviderListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.date_type


class SAMLProviderListEntry(TypedDict, closed=True):
    arn: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) of the SAML provider.</p>"""
    valid_until: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The expiration date and time for the SAML provider.</p>"""
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time when the SAML provider was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SAMLProviderListEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "valid_until" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["valid_until"], pairs, f"{prefix}.ValidUntil"
        )
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )


def deserialize_query(el: Element) -> SAMLProviderListEntry:
    out: SAMLProviderListEntry = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_valid_until = el.find("ValidUntil")
    if child_valid_until is not None:
        import capo_iam.types.date_type

        out["valid_until"] = capo_iam.types.date_type.deserialize_query(
            child_valid_until
        )
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    return out
