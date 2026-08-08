"""Generated from Smithy shape ``com.amazonaws.ec2#Reservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.instance_list
    import capo_ec2.types.string


class Reservation(TypedDict, closed=True):
    reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the reservation.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the reservation.</p>"""
    requester_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the requester that launched the instances on your behalf (for example, Amazon Web Services Management Console or Auto Scaling).</p>"""
    groups: NotRequired["capo_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>Not supported.</p>"""
    instances: NotRequired["capo_ec2.types.instance_list.InstanceList"]
    """<p>The instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Reservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reservation_id" in value:
        pairs.append((f"{key_prefix}ReservationId", str(value["reservation_id"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "requester_id" in value:
        pairs.append((f"{key_prefix}RequesterId", str(value["requester_id"])))
    if "groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "instances" in value:
        import capo_ec2.types.instance_list

        capo_ec2.types.instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}InstancesSet"
        )


def deserialize_ec2_query(el: Element) -> Reservation:
    out: Reservation = {}  # type: ignore[typeddict-item]
    child_reservation_id = el.find("reservationId")
    if child_reservation_id is not None:
        out["reservation_id"] = str(child_reservation_id.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_requester_id = el.find("requesterId")
    if child_requester_id is not None:
        out["requester_id"] = str(child_requester_id.text or "")
    if el.find("groupSet") is not None:
        import capo_ec2.types.group_identifier_list

        out["groups"] = capo_ec2.types.group_identifier_list.deserialize_ec2_query(
            el, "groupSet"
        )
    if el.find("instancesSet") is not None:
        import capo_ec2.types.instance_list

        out["instances"] = capo_ec2.types.instance_list.deserialize_ec2_query(
            el, "instancesSet"
        )
    return out
