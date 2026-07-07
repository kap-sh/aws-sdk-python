"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CapacityUsageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.cidr_summary


class CapacityUsageSummary(TypedDict, closed=True):
    cid_rs: NotRequired["aws_sdk_network_firewall.types.cidr_summary.CIDRSummary"]
    """<p>Describes the capacity usage of the CIDR blocks used by the IP set references in a firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityUsageSummary) -> dict:
    out: dict = {}
    if "cid_rs" in value:
        import aws_sdk_network_firewall.types.cidr_summary

        out["CIDRs"] = (
            aws_sdk_network_firewall.types.cidr_summary.serialize_aws_json_1_0(
                value["cid_rs"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityUsageSummary:
    out: CapacityUsageSummary = {}  # type: ignore[typeddict-item]
    if "CIDRs" in data:
        import aws_sdk_network_firewall.types.cidr_summary

        out["cid_rs"] = (
            aws_sdk_network_firewall.types.cidr_summary.deserialize_aws_json_1_0(
                data["CIDRs"]
            )
        )
    return out
