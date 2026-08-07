"""Generated from Smithy shape ``com.amazonaws.ses#ListVerifiedEmailAddressesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.address_list


class ListVerifiedEmailAddressesResponse(TypedDict, closed=True):
    verified_email_addresses: NotRequired["capo_ses.types.address_list.AddressList"]
    """<p>A list of email addresses that have been verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListVerifiedEmailAddressesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_email_addresses" in value:
        import capo_ses.types.address_list

        capo_ses.types.address_list.serialize_query(
            value["verified_email_addresses"],
            pairs,
            f"{key_prefix}VerifiedEmailAddresses",
        )


def deserialize_query(el: Element) -> ListVerifiedEmailAddressesResponse:
    out: ListVerifiedEmailAddressesResponse = {}  # type: ignore[typeddict-item]
    child_verified_email_addresses = el.find("VerifiedEmailAddresses")
    if child_verified_email_addresses is not None:
        import capo_ses.types.address_list

        out["verified_email_addresses"] = capo_ses.types.address_list.deserialize_query(
            child_verified_email_addresses
        )
    return out
