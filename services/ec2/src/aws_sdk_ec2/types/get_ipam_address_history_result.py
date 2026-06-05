"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamAddressHistoryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_address_history_record_set
    import aws_sdk_ec2.types.next_token


class GetIpamAddressHistoryResult(TypedDict):
    history_records: NotRequired[
        "aws_sdk_ec2.types.ipam_address_history_record_set.IpamAddressHistoryRecordSet"
    ]
    """<p>A historical record for a CIDR within an IPAM scope. If the CIDR is associated with an EC2 instance, you will see an object in the response for the instance and one for the network interface.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamAddressHistoryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "history_records" in value:
        import aws_sdk_ec2.types.ipam_address_history_record_set

        aws_sdk_ec2.types.ipam_address_history_record_set.serialize_ec2_query(
            value["history_records"], pairs, f"{prefix}.HistoryRecordSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamAddressHistoryResult:
    out: GetIpamAddressHistoryResult = {}  # type: ignore[typeddict-item]
    if el.find("HistoryRecordSet") is not None:
        import aws_sdk_ec2.types.ipam_address_history_record_set

        out["history_records"] = (
            aws_sdk_ec2.types.ipam_address_history_record_set.deserialize_ec2_query(
                el, "HistoryRecordSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
