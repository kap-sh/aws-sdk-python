"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetCidrReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_reservation_type
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list


class CreateSubnetCidrReservationRequest(TypedDict, closed=True):
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 or IPV6 CIDR range to reserve.</p>"""
    reservation_type: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_type.SubnetCidrReservationType"
    ]
    """<p>The type of reservation. The reservation type determines how the reserved IP addresses are assigned to resources.</p> <ul> <li> <p> <code>prefix</code> - Amazon Web Services assigns the reserved IP addresses to network interfaces.</p> </li> <li> <p> <code>explicit</code> - You assign the reserved IP addresses to network interfaces.</p> </li> </ul>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description to assign to the subnet CIDR reservation.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the subnet CIDR reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSubnetCidrReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "reservation_type" in value:
        import aws_sdk_ec2.types.subnet_cidr_reservation_type

        aws_sdk_ec2.types.subnet_cidr_reservation_type.serialize_ec2_query(
            value["reservation_type"], pairs, f"{prefix}.ReservationType"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateSubnetCidrReservationRequest:
    out: CreateSubnetCidrReservationRequest = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_reservation_type = el.find("ReservationType")
    if child_reservation_type is not None:
        import aws_sdk_ec2.types.subnet_cidr_reservation_type

        out["reservation_type"] = (
            aws_sdk_ec2.types.subnet_cidr_reservation_type.deserialize_ec2_query(
                child_reservation_type
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
