"""Generated from Smithy shape ``com.amazonaws.ec2#AddressTransfer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_transfer_status
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class AddressTransfer(TypedDict, closed=True):
    public_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The Elastic IP address being transferred.</p>"""
    allocation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The allocation ID of an Elastic IP address.</p>"""
    transfer_account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the account that you want to transfer the Elastic IP address to.</p>"""
    transfer_offer_expiration_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp when the Elastic IP address transfer expired. When the source account starts the transfer, the transfer account has seven hours to allocate the Elastic IP address to complete the transfer, or the Elastic IP address will return to its original owner.</p>"""
    transfer_offer_accepted_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp when the Elastic IP address transfer was accepted.</p>"""
    address_transfer_status: NotRequired[
        "capo_ec2.types.address_transfer_status.AddressTransferStatus"
    ]
    """<p>The Elastic IP address transfer status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddressTransfer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "public_ip" in value:
        pairs.append((f"{key_prefix}PublicIp", str(value["public_ip"])))
    if "allocation_id" in value:
        pairs.append((f"{key_prefix}AllocationId", str(value["allocation_id"])))
    if "transfer_account_id" in value:
        pairs.append(
            (f"{key_prefix}TransferAccountId", str(value["transfer_account_id"]))
        )
    if "transfer_offer_expiration_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["transfer_offer_expiration_timestamp"],
            pairs,
            f"{key_prefix}TransferOfferExpirationTimestamp",
        )
    if "transfer_offer_accepted_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["transfer_offer_accepted_timestamp"],
            pairs,
            f"{key_prefix}TransferOfferAcceptedTimestamp",
        )
    if "address_transfer_status" in value:
        import capo_ec2.types.address_transfer_status

        capo_ec2.types.address_transfer_status.serialize_ec2_query(
            value["address_transfer_status"],
            pairs,
            f"{key_prefix}AddressTransferStatus",
        )


def deserialize_ec2_query(el: Element) -> AddressTransfer:
    out: AddressTransfer = {}  # type: ignore[typeddict-item]
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_transfer_account_id = el.find("TransferAccountId")
    if child_transfer_account_id is not None:
        out["transfer_account_id"] = str(child_transfer_account_id.text or "")
    child_transfer_offer_expiration_timestamp = el.find(
        "TransferOfferExpirationTimestamp"
    )
    if child_transfer_offer_expiration_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["transfer_offer_expiration_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_transfer_offer_expiration_timestamp
            )
        )
    child_transfer_offer_accepted_timestamp = el.find("TransferOfferAcceptedTimestamp")
    if child_transfer_offer_accepted_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["transfer_offer_accepted_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_transfer_offer_accepted_timestamp
            )
        )
    child_address_transfer_status = el.find("AddressTransferStatus")
    if child_address_transfer_status is not None:
        import capo_ec2.types.address_transfer_status

        out["address_transfer_status"] = (
            capo_ec2.types.address_transfer_status.deserialize_ec2_query(
                child_address_transfer_status
            )
        )
    return out
