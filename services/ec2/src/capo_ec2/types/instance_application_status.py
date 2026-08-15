"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceApplicationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status
    import capo_ec2.types.instance_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class InstanceApplicationStatus(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the instance.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone of the instance.</p>"""
    application_status: NotRequired[
        "capo_ec2.types.application_status.ApplicationStatus"
    ]
    """<p>The application status for the instance.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceApplicationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "application_status" in value:
        import capo_ec2.types.application_status

        capo_ec2.types.application_status.serialize_ec2_query(
            value["application_status"], pairs, f"{key_prefix}ApplicationStatus"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> InstanceApplicationStatus:
    out: InstanceApplicationStatus = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_application_status = el.find("applicationStatus")
    if child_application_status is not None:
        import capo_ec2.types.application_status

        out["application_status"] = (
            capo_ec2.types.application_status.deserialize_ec2_query(
                child_application_status
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
