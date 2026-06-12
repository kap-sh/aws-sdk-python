"""Generated from Smithy shape ``com.amazonaws.ses#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.address_list


class Destination(TypedDict):
    to_addresses: NotRequired["aws_sdk_ses.types.address_list.AddressList"]
    """<p>The recipients to place on the To: line of the message.</p>"""
    cc_addresses: NotRequired["aws_sdk_ses.types.address_list.AddressList"]
    """<p>The recipients to place on the CC: line of the message.</p>"""
    bcc_addresses: NotRequired["aws_sdk_ses.types.address_list.AddressList"]
    """<p>The recipients to place on the BCC: line of the message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Destination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "to_addresses" in value:
        import aws_sdk_ses.types.address_list

        aws_sdk_ses.types.address_list.serialize_query(
            value["to_addresses"], pairs, f"{prefix}.ToAddresses"
        )
    if "cc_addresses" in value:
        import aws_sdk_ses.types.address_list

        aws_sdk_ses.types.address_list.serialize_query(
            value["cc_addresses"], pairs, f"{prefix}.CcAddresses"
        )
    if "bcc_addresses" in value:
        import aws_sdk_ses.types.address_list

        aws_sdk_ses.types.address_list.serialize_query(
            value["bcc_addresses"], pairs, f"{prefix}.BccAddresses"
        )


def deserialize_query(el: Element) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    child_to_addresses = el.find("ToAddresses")
    if child_to_addresses is not None:
        import aws_sdk_ses.types.address_list

        out["to_addresses"] = aws_sdk_ses.types.address_list.deserialize_query(
            child_to_addresses
        )
    child_cc_addresses = el.find("CcAddresses")
    if child_cc_addresses is not None:
        import aws_sdk_ses.types.address_list

        out["cc_addresses"] = aws_sdk_ses.types.address_list.deserialize_query(
            child_cc_addresses
        )
    child_bcc_addresses = el.find("BccAddresses")
    if child_bcc_addresses is not None:
        import aws_sdk_ses.types.address_list

        out["bcc_addresses"] = aws_sdk_ses.types.address_list.deserialize_query(
            child_bcc_addresses
        )
    return out
