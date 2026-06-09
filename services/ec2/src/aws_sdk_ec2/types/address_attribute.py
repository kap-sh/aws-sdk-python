"""Generated from Smithy shape ``com.amazonaws.ec2#AddressAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.ptr_update_status
    import aws_sdk_ec2.types.public_ip_address
    import aws_sdk_ec2.types.string


class AddressAttribute(TypedDict):
    public_ip: NotRequired["aws_sdk_ec2.types.public_ip_address.PublicIpAddress"]
    """<p>The public IP address.</p>"""
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>[EC2-VPC] The allocation ID.</p>"""
    ptr_record: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The pointer (PTR) record for the IP address.</p>"""
    ptr_record_update: NotRequired[
        "aws_sdk_ec2.types.ptr_update_status.PtrUpdateStatus"
    ]
    """<p>The updated PTR record for the IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddressAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "ptr_record" in value:
        pairs.append((f"{prefix}.PtrRecord", str(value["ptr_record"])))
    if "ptr_record_update" in value:
        import aws_sdk_ec2.types.ptr_update_status

        aws_sdk_ec2.types.ptr_update_status.serialize_ec2_query(
            value["ptr_record_update"], pairs, f"{prefix}.PtrRecordUpdate"
        )


def deserialize_ec2_query(el: Element) -> AddressAttribute:
    out: AddressAttribute = {}  # type: ignore[typeddict-item]
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_ptr_record = el.find("PtrRecord")
    if child_ptr_record is not None:
        out["ptr_record"] = str(child_ptr_record.text or "")
    child_ptr_record_update = el.find("PtrRecordUpdate")
    if child_ptr_record_update is not None:
        import aws_sdk_ec2.types.ptr_update_status

        out["ptr_record_update"] = (
            aws_sdk_ec2.types.ptr_update_status.deserialize_ec2_query(
                child_ptr_record_update
            )
        )
    return out
