"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.ebs_status_summary
    import capo_ec2.types.instance_state
    import capo_ec2.types.instance_status_event_list
    import capo_ec2.types.instance_status_summary
    import capo_ec2.types.operator_response
    import capo_ec2.types.string


class InstanceStatus(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the instance.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the instance.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the instance.</p>"""
    events: NotRequired[
        "capo_ec2.types.instance_status_event_list.InstanceStatusEventList"
    ]
    """<p>Any scheduled events associated with the instance.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_state: NotRequired["capo_ec2.types.instance_state.InstanceState"]
    """<p>The intended state of the instance. <a>DescribeInstanceStatus</a> requires that an instance be in the <code>running</code> state.</p>"""
    instance_status: NotRequired[
        "capo_ec2.types.instance_status_summary.InstanceStatusSummary"
    ]
    """<p>Reports impaired functionality that stems from issues internal to the instance, such as impaired reachability.</p>"""
    system_status: NotRequired[
        "capo_ec2.types.instance_status_summary.InstanceStatusSummary"
    ]
    """<p>Reports impaired functionality that stems from issues related to the systems that support an instance, such as hardware failures and network connectivity problems.</p>"""
    attached_ebs_status: NotRequired[
        "capo_ec2.types.ebs_status_summary.EbsStatusSummary"
    ]
    """<p>Reports impaired functionality that stems from an attached Amazon EBS volume that is unreachable and unable to complete I/O operations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{prefix}.Operator"
        )
    if "events" in value:
        import capo_ec2.types.instance_status_event_list

        capo_ec2.types.instance_status_event_list.serialize_ec2_query(
            value["events"], pairs, f"{prefix}.EventsSet"
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "instance_state" in value:
        import capo_ec2.types.instance_state

        capo_ec2.types.instance_state.serialize_ec2_query(
            value["instance_state"], pairs, f"{prefix}.InstanceState"
        )
    if "instance_status" in value:
        import capo_ec2.types.instance_status_summary

        capo_ec2.types.instance_status_summary.serialize_ec2_query(
            value["instance_status"], pairs, f"{prefix}.InstanceStatus"
        )
    if "system_status" in value:
        import capo_ec2.types.instance_status_summary

        capo_ec2.types.instance_status_summary.serialize_ec2_query(
            value["system_status"], pairs, f"{prefix}.SystemStatus"
        )
    if "attached_ebs_status" in value:
        import capo_ec2.types.ebs_status_summary

        capo_ec2.types.ebs_status_summary.serialize_ec2_query(
            value["attached_ebs_status"], pairs, f"{prefix}.AttachedEbsStatus"
        )


def deserialize_ec2_query(el: Element) -> InstanceStatus:
    out: InstanceStatus = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    if el.find("EventsSet") is not None:
        import capo_ec2.types.instance_status_event_list

        out["events"] = capo_ec2.types.instance_status_event_list.deserialize_ec2_query(
            el, "EventsSet"
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_state = el.find("InstanceState")
    if child_instance_state is not None:
        import capo_ec2.types.instance_state

        out["instance_state"] = capo_ec2.types.instance_state.deserialize_ec2_query(
            child_instance_state
        )
    child_instance_status = el.find("InstanceStatus")
    if child_instance_status is not None:
        import capo_ec2.types.instance_status_summary

        out["instance_status"] = (
            capo_ec2.types.instance_status_summary.deserialize_ec2_query(
                child_instance_status
            )
        )
    child_system_status = el.find("SystemStatus")
    if child_system_status is not None:
        import capo_ec2.types.instance_status_summary

        out["system_status"] = (
            capo_ec2.types.instance_status_summary.deserialize_ec2_query(
                child_system_status
            )
        )
    child_attached_ebs_status = el.find("AttachedEbsStatus")
    if child_attached_ebs_status is not None:
        import capo_ec2.types.ebs_status_summary

        out["attached_ebs_status"] = (
            capo_ec2.types.ebs_status_summary.deserialize_ec2_query(
                child_attached_ebs_status
            )
        )
    return out
