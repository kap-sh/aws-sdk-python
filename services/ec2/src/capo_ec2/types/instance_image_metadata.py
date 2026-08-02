"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceImageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_metadata
    import capo_ec2.types.instance_id
    import capo_ec2.types.instance_state
    import capo_ec2.types.instance_type
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.operator_response
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class InstanceImageMetadata(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    launch_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time the instance was launched.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone of the instance.</p>"""
    zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone or Local Zone of the instance.</p>"""
    state: NotRequired["capo_ec2.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the instance.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the instance.</p>"""
    image_metadata: NotRequired["capo_ec2.types.image_metadata.ImageMetadata"]
    """<p>Information about the AMI used to launch the instance.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceImageMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "launch_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["launch_time"], pairs, f"{key_prefix}LaunchTime"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "zone_id" in value:
        pairs.append((f"{key_prefix}ZoneId", str(value["zone_id"])))
    if "state" in value:
        import capo_ec2.types.instance_state

        capo_ec2.types.instance_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}InstanceState"
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}InstanceOwnerId", str(value["owner_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "image_metadata" in value:
        import capo_ec2.types.image_metadata

        capo_ec2.types.image_metadata.serialize_ec2_query(
            value["image_metadata"], pairs, f"{key_prefix}ImageMetadata"
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_ec2_query(el: Element) -> InstanceImageMetadata:
    out: InstanceImageMetadata = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_launch_time = el.find("LaunchTime")
    if child_launch_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["launch_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_launch_time
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_zone_id = el.find("ZoneId")
    if child_zone_id is not None:
        out["zone_id"] = str(child_zone_id.text or "")
    child_state = el.find("InstanceState")
    if child_state is not None:
        import capo_ec2.types.instance_state

        out["state"] = capo_ec2.types.instance_state.deserialize_ec2_query(child_state)
    child_owner_id = el.find("InstanceOwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_image_metadata = el.find("ImageMetadata")
    if child_image_metadata is not None:
        import capo_ec2.types.image_metadata

        out["image_metadata"] = capo_ec2.types.image_metadata.deserialize_ec2_query(
            child_image_metadata
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out
