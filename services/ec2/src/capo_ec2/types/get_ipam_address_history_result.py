"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamAddressHistoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_address_history_record_set
    import capo_ec2.types.next_token


class GetIpamAddressHistoryResult(TypedDict, closed=True):
    history_records: NotRequired[
        "capo_ec2.types.ipam_address_history_record_set.IpamAddressHistoryRecordSet"
    ]
    """<p>A historical record for a CIDR within an IPAM scope. If the CIDR is associated with an EC2 instance, you will see an object in the response for the instance and one for the network interface.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamAddressHistoryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "history_records" in value:
        import capo_ec2.types.ipam_address_history_record_set

        capo_ec2.types.ipam_address_history_record_set.serialize_ec2_query(
            value["history_records"], pairs, f"{key_prefix}HistoryRecordSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamAddressHistoryResult:
    out: GetIpamAddressHistoryResult = {}  # type: ignore[typeddict-item]
    child_history_records = el.find("historyRecordSet")
    if child_history_records is not None:
        import capo_ec2.types.ipam_address_history_record_set

        out["history_records"] = (
            capo_ec2.types.ipam_address_history_record_set.deserialize_ec2_query(
                child_history_records
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
