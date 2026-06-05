"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.capacity_allocations
    import aws_sdk_ec2.types.capacity_block_id
    import aws_sdk_ec2.types.capacity_reservation_commitment_info
    import aws_sdk_ec2.types.capacity_reservation_delivery_preference
    import aws_sdk_ec2.types.capacity_reservation_instance_platform
    import aws_sdk_ec2.types.capacity_reservation_state
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.capacity_reservation_type
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.end_date_type
    import aws_sdk_ec2.types.instance_match_criteria
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_allocation
    import aws_sdk_ec2.types.interruption_info
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.outpost_arn
    import aws_sdk_ec2.types.placement_group_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CapacityReservation(TypedDict):
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Capacity Reservation.</p>"""
    capacity_reservation_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the capacity is reserved.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of instance for which the Capacity Reservation reserves capacity.</p>"""
    instance_platform: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which the Capacity Reservation reserves capacity.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the capacity is reserved.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    total_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of instances for which the Capacity Reservation reserves capacity.</p>"""
    available_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.</p>"""
    ephemeral_storage: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> <i>Deprecated.</i> </p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_state.CapacityReservationState"
    ]
    """<p>The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:</p> <ul> <li> <p> <code>active</code> - The capacity is available for use.</p> </li> <li> <p> <code>expired</code> - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>cancelled</code> - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>pending</code> - The Capacity Reservation request was successful but the capacity provisioning is still pending.</p> </li> <li> <p> <code>failed</code> - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.</p> </li> <li> <p> <code>scheduled</code> - (<i>Future-dated Capacity Reservations</i>) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.</p> </li> <li> <p> <code>payment-pending</code> - (<i>Capacity Blocks</i>) The upfront payment has not been processed yet.</p> </li> <li> <p> <code>payment-failed</code> - (<i>Capacity Blocks</i>) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.</p> </li> <li> <p> <code>assessing</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.</p> </li> <li> <p> <code>delayed</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.</p> </li> <li> <p> <code>unsupported</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.</p> </li> </ul>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the Capacity Reservation was started.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p>"""
    end_date_type: NotRequired["aws_sdk_ec2.types.end_date_type.EndDateType"]
    """<p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time.</p> </li> </ul>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.instance_match_criteria.InstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation accepts. The options include:</p> <ul> <li> <p> <code>open</code> - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.</p> </li> <li> <p> <code>targeted</code> - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity. </p> </li> </ul>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the Capacity Reservation was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Capacity Reservation.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.outpost_arn.OutpostArn"]
    """<p>The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.</p>"""
    capacity_reservation_fleet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet.</p>"""
    placement_group_arn: NotRequired[
        "aws_sdk_ec2.types.placement_group_arn.PlacementGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster placement group in which the Capacity Reservation was created. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html\"> Capacity Reservations for cluster placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_allocations: NotRequired[
        "aws_sdk_ec2.types.capacity_allocations.CapacityAllocations"
    ]
    """<p>Information about instance capacity usage.</p>"""
    reservation_type: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_type.CapacityReservationType"
    ]
    """<p>The type of Capacity Reservation.</p>"""
    unused_reservation_billing_owner_id: NotRequired[
        "aws_sdk_ec2.types.account_id.AccountID"
    ]
    """<p>The ID of the Amazon Web Services account to which billing of the unused capacity of the Capacity Reservation is assigned.</p>"""
    commitment_info: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_commitment_info.CapacityReservationCommitmentInfo"
    ]
    """<p>Information about your commitment for a future-dated Capacity Reservation.</p>"""
    delivery_preference: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_delivery_preference.CapacityReservationDeliveryPreference"
    ]
    """<p>The delivery method for a future-dated Capacity Reservation. <code>incremental</code> indicates that the requested capacity is delivered in addition to any running instances and reserved capacity that you have in your account at the requested date and time.</p>"""
    capacity_block_id: NotRequired[
        "aws_sdk_ec2.types.capacity_block_id.CapacityBlockId"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    interruptible: NotRequired["aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p> Indicates whether this Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims capacity. </p>"""
    interruptible_capacity_allocation: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_allocation.InterruptibleCapacityAllocation"
    ]
    """<p> Contains allocation details for interruptible reservations, including current allocated instances and target instance counts within the interruptibleCapacityAllocation object. </p>"""
    interruption_info: NotRequired[
        "aws_sdk_ec2.types.interruption_info.InterruptionInfo"
    ]
    """<p> Information about the interruption configuration and association with the source reservation for interruptible Capacity Reservations. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "capacity_reservation_arn" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationArn", str(value["capacity_reservation_arn"]))
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "instance_platform" in value:
        import aws_sdk_ec2.types.capacity_reservation_instance_platform

        aws_sdk_ec2.types.capacity_reservation_instance_platform.serialize_ec2_query(
            value["instance_platform"], pairs, f"{prefix}.InstancePlatform"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "tenancy" in value:
        import aws_sdk_ec2.types.capacity_reservation_tenancy

        aws_sdk_ec2.types.capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "total_instance_count" in value:
        pairs.append(
            (f"{prefix}.TotalInstanceCount", str(value["total_instance_count"]))
        )
    if "available_instance_count" in value:
        pairs.append(
            (f"{prefix}.AvailableInstanceCount", str(value["available_instance_count"]))
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{prefix}.EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "ephemeral_storage" in value:
        pairs.append(
            (
                f"{prefix}.EphemeralStorage",
                "true" if value["ephemeral_storage"] else "false",
            )
        )
    if "state" in value:
        import aws_sdk_ec2.types.capacity_reservation_state

        aws_sdk_ec2.types.capacity_reservation_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "start_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "end_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "end_date_type" in value:
        import aws_sdk_ec2.types.end_date_type

        aws_sdk_ec2.types.end_date_type.serialize_ec2_query(
            value["end_date_type"], pairs, f"{prefix}.EndDateType"
        )
    if "instance_match_criteria" in value:
        import aws_sdk_ec2.types.instance_match_criteria

        aws_sdk_ec2.types.instance_match_criteria.serialize_ec2_query(
            value["instance_match_criteria"], pairs, f"{prefix}.InstanceMatchCriteria"
        )
    if "create_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "capacity_reservation_fleet_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityReservationFleetId",
                str(value["capacity_reservation_fleet_id"]),
            )
        )
    if "placement_group_arn" in value:
        pairs.append((f"{prefix}.PlacementGroupArn", str(value["placement_group_arn"])))
    if "capacity_allocations" in value:
        import aws_sdk_ec2.types.capacity_allocations

        aws_sdk_ec2.types.capacity_allocations.serialize_ec2_query(
            value["capacity_allocations"], pairs, f"{prefix}.CapacityAllocationSet"
        )
    if "reservation_type" in value:
        import aws_sdk_ec2.types.capacity_reservation_type

        aws_sdk_ec2.types.capacity_reservation_type.serialize_ec2_query(
            value["reservation_type"], pairs, f"{prefix}.ReservationType"
        )
    if "unused_reservation_billing_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.UnusedReservationBillingOwnerId",
                str(value["unused_reservation_billing_owner_id"]),
            )
        )
    if "commitment_info" in value:
        import aws_sdk_ec2.types.capacity_reservation_commitment_info

        aws_sdk_ec2.types.capacity_reservation_commitment_info.serialize_ec2_query(
            value["commitment_info"], pairs, f"{prefix}.CommitmentInfo"
        )
    if "delivery_preference" in value:
        import aws_sdk_ec2.types.capacity_reservation_delivery_preference

        aws_sdk_ec2.types.capacity_reservation_delivery_preference.serialize_ec2_query(
            value["delivery_preference"], pairs, f"{prefix}.DeliveryPreference"
        )
    if "capacity_block_id" in value:
        pairs.append((f"{prefix}.CapacityBlockId", str(value["capacity_block_id"])))
    if "interruptible" in value:
        pairs.append(
            (f"{prefix}.Interruptible", "true" if value["interruptible"] else "false")
        )
    if "interruptible_capacity_allocation" in value:
        import aws_sdk_ec2.types.interruptible_capacity_allocation

        aws_sdk_ec2.types.interruptible_capacity_allocation.serialize_ec2_query(
            value["interruptible_capacity_allocation"],
            pairs,
            f"{prefix}.InterruptibleCapacityAllocation",
        )
    if "interruption_info" in value:
        import aws_sdk_ec2.types.interruption_info

        aws_sdk_ec2.types.interruption_info.serialize_ec2_query(
            value["interruption_info"], pairs, f"{prefix}.InterruptionInfo"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservation:
    out: CapacityReservation = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_capacity_reservation_arn = el.find("CapacityReservationArn")
    if child_capacity_reservation_arn is not None:
        out["capacity_reservation_arn"] = str(child_capacity_reservation_arn.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_platform = el.find("InstancePlatform")
    if child_instance_platform is not None:
        import aws_sdk_ec2.types.capacity_reservation_instance_platform

        out["instance_platform"] = (
            aws_sdk_ec2.types.capacity_reservation_instance_platform.deserialize_ec2_query(
                child_instance_platform
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import aws_sdk_ec2.types.capacity_reservation_tenancy

        out["tenancy"] = (
            aws_sdk_ec2.types.capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_total_instance_count = el.find("TotalInstanceCount")
    if child_total_instance_count is not None:
        out["total_instance_count"] = int(child_total_instance_count.text or "")
    child_available_instance_count = el.find("AvailableInstanceCount")
    if child_available_instance_count is not None:
        out["available_instance_count"] = int(child_available_instance_count.text or "")
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_ephemeral_storage = el.find("EphemeralStorage")
    if child_ephemeral_storage is not None:
        out["ephemeral_storage"] = (
            child_ephemeral_storage.text or ""
        ).lower() == "true"
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.capacity_reservation_state

        out["state"] = (
            aws_sdk_ec2.types.capacity_reservation_state.deserialize_ec2_query(
                child_state
            )
        )
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["start_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_date
            )
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import aws_sdk_ec2.types.date_time

        out["end_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_end_date
        )
    child_end_date_type = el.find("EndDateType")
    if child_end_date_type is not None:
        import aws_sdk_ec2.types.end_date_type

        out["end_date_type"] = aws_sdk_ec2.types.end_date_type.deserialize_ec2_query(
            child_end_date_type
        )
    child_instance_match_criteria = el.find("InstanceMatchCriteria")
    if child_instance_match_criteria is not None:
        import aws_sdk_ec2.types.instance_match_criteria

        out["instance_match_criteria"] = (
            aws_sdk_ec2.types.instance_match_criteria.deserialize_ec2_query(
                child_instance_match_criteria
            )
        )
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_ec2.types.date_time

        out["create_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_date
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_capacity_reservation_fleet_id = el.find("CapacityReservationFleetId")
    if child_capacity_reservation_fleet_id is not None:
        out["capacity_reservation_fleet_id"] = str(
            child_capacity_reservation_fleet_id.text or ""
        )
    child_placement_group_arn = el.find("PlacementGroupArn")
    if child_placement_group_arn is not None:
        out["placement_group_arn"] = str(child_placement_group_arn.text or "")
    if el.find("CapacityAllocationSet") is not None:
        import aws_sdk_ec2.types.capacity_allocations

        out["capacity_allocations"] = (
            aws_sdk_ec2.types.capacity_allocations.deserialize_ec2_query(
                el, "CapacityAllocationSet"
            )
        )
    child_reservation_type = el.find("ReservationType")
    if child_reservation_type is not None:
        import aws_sdk_ec2.types.capacity_reservation_type

        out["reservation_type"] = (
            aws_sdk_ec2.types.capacity_reservation_type.deserialize_ec2_query(
                child_reservation_type
            )
        )
    child_unused_reservation_billing_owner_id = el.find(
        "UnusedReservationBillingOwnerId"
    )
    if child_unused_reservation_billing_owner_id is not None:
        out["unused_reservation_billing_owner_id"] = str(
            child_unused_reservation_billing_owner_id.text or ""
        )
    child_commitment_info = el.find("CommitmentInfo")
    if child_commitment_info is not None:
        import aws_sdk_ec2.types.capacity_reservation_commitment_info

        out["commitment_info"] = (
            aws_sdk_ec2.types.capacity_reservation_commitment_info.deserialize_ec2_query(
                child_commitment_info
            )
        )
    child_delivery_preference = el.find("DeliveryPreference")
    if child_delivery_preference is not None:
        import aws_sdk_ec2.types.capacity_reservation_delivery_preference

        out["delivery_preference"] = (
            aws_sdk_ec2.types.capacity_reservation_delivery_preference.deserialize_ec2_query(
                child_delivery_preference
            )
        )
    child_capacity_block_id = el.find("CapacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    child_interruptible = el.find("Interruptible")
    if child_interruptible is not None:
        out["interruptible"] = (child_interruptible.text or "").lower() == "true"
    child_interruptible_capacity_allocation = el.find("InterruptibleCapacityAllocation")
    if child_interruptible_capacity_allocation is not None:
        import aws_sdk_ec2.types.interruptible_capacity_allocation

        out["interruptible_capacity_allocation"] = (
            aws_sdk_ec2.types.interruptible_capacity_allocation.deserialize_ec2_query(
                child_interruptible_capacity_allocation
            )
        )
    child_interruption_info = el.find("InterruptionInfo")
    if child_interruption_info is not None:
        import aws_sdk_ec2.types.interruption_info

        out["interruption_info"] = (
            aws_sdk_ec2.types.interruption_info.deserialize_ec2_query(
                child_interruption_info
            )
        )
    return out
