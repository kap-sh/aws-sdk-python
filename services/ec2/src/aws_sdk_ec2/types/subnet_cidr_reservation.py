"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetCidrReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_reservation_id
    import aws_sdk_ec2.types.subnet_cidr_reservation_type
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_list


class SubnetCidrReservation(TypedDict, closed=True):
    subnet_cidr_reservation_id: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_id.SubnetCidrReservationId"
    ]
    """<p>The ID of the subnet CIDR reservation.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR that has been reserved.</p>"""
    reservation_type: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation_type.SubnetCidrReservationType"
    ]
    """<p>The type of reservation. </p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that owns the subnet CIDR reservation. </p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description assigned to the subnet CIDR reservation.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the subnet CIDR reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetCidrReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_cidr_reservation_id" in value:
        pairs.append(
            (
                f"{prefix}.SubnetCidrReservationId",
                str(value["subnet_cidr_reservation_id"]),
            )
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "reservation_type" in value:
        import aws_sdk_ec2.types.subnet_cidr_reservation_type

        aws_sdk_ec2.types.subnet_cidr_reservation_type.serialize_ec2_query(
            value["reservation_type"], pairs, f"{prefix}.ReservationType"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> SubnetCidrReservation:
    out: SubnetCidrReservation = {}  # type: ignore[typeddict-item]
    child_subnet_cidr_reservation_id = el.find("SubnetCidrReservationId")
    if child_subnet_cidr_reservation_id is not None:
        out["subnet_cidr_reservation_id"] = str(
            child_subnet_cidr_reservation_id.text or ""
        )
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
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
