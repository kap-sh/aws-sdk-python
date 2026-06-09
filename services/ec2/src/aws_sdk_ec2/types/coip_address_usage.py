"""Generated from Smithy shape ``com.amazonaws.ec2#CoipAddressUsage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CoipAddressUsage(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID of the address.</p>"""
    aws_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    aws_service: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services service.</p>"""
    co_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CoipAddressUsage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "aws_account_id" in value:
        pairs.append((f"{prefix}.AwsAccountId", str(value["aws_account_id"])))
    if "aws_service" in value:
        pairs.append((f"{prefix}.AwsService", str(value["aws_service"])))
    if "co_ip" in value:
        pairs.append((f"{prefix}.CoIp", str(value["co_ip"])))


def deserialize_ec2_query(el: Element) -> CoipAddressUsage:
    out: CoipAddressUsage = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_aws_account_id = el.find("AwsAccountId")
    if child_aws_account_id is not None:
        out["aws_account_id"] = str(child_aws_account_id.text or "")
    child_aws_service = el.find("AwsService")
    if child_aws_service is not None:
        out["aws_service"] = str(child_aws_service.text or "")
    child_co_ip = el.find("CoIp")
    if child_co_ip is not None:
        out["co_ip"] = str(child_co_ip.text or "")
    return out
