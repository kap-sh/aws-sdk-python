"""Generated from Smithy shape ``com.amazonaws.ses#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.address_list


class Destination(TypedDict, closed=True):
    to_addresses: NotRequired["capo_ses.types.address_list.AddressList"]
    """<p>The recipients to place on the To: line of the message.</p>"""
    cc_addresses: NotRequired["capo_ses.types.address_list.AddressList"]
    """<p>The recipients to place on the CC: line of the message.</p>"""
    bcc_addresses: NotRequired["capo_ses.types.address_list.AddressList"]
    """<p>The recipients to place on the BCC: line of the message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Destination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "to_addresses" in value:
        import capo_ses.types.address_list

        capo_ses.types.address_list.serialize_query(
            value["to_addresses"], pairs, f"{key_prefix}ToAddresses"
        )
    if "cc_addresses" in value:
        import capo_ses.types.address_list

        capo_ses.types.address_list.serialize_query(
            value["cc_addresses"], pairs, f"{key_prefix}CcAddresses"
        )
    if "bcc_addresses" in value:
        import capo_ses.types.address_list

        capo_ses.types.address_list.serialize_query(
            value["bcc_addresses"], pairs, f"{key_prefix}BccAddresses"
        )


def deserialize_query(el: Element) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    child_to_addresses = el.find("ToAddresses")
    if child_to_addresses is not None:
        import capo_ses.types.address_list

        out["to_addresses"] = capo_ses.types.address_list.deserialize_query(
            child_to_addresses
        )
    child_cc_addresses = el.find("CcAddresses")
    if child_cc_addresses is not None:
        import capo_ses.types.address_list

        out["cc_addresses"] = capo_ses.types.address_list.deserialize_query(
            child_cc_addresses
        )
    child_bcc_addresses = el.find("BccAddresses")
    if child_bcc_addresses is not None:
        import capo_ses.types.address_list

        out["bcc_addresses"] = capo_ses.types.address_list.deserialize_query(
            child_bcc_addresses
        )
    return out
