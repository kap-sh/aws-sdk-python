"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_tag_dimension_set
    import capo_ec2.types.capacity_tenancy
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.reservation_end_date_type
    import capo_ec2.types.reservation_state
    import capo_ec2.types.reservation_type
    import capo_ec2.types.string


class CapacityManagerDimension(TypedDict, closed=True):
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p> The Amazon Web Services Region where the capacity resource is located. </p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The unique identifier of the Availability Zone where the capacity resource is located. </p>"""
    account_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The Amazon Web Services account ID that owns the capacity resource. </p>"""
    account_name: NotRequired["capo_ec2.types.string.String"]
    """<p> The name of the Amazon Web Services account that owns the capacity resource. This dimension is only available when Organizations access is enabled for Capacity Manager. </p>"""
    instance_family: NotRequired["capo_ec2.types.string.String"]
    """<p> The EC2 instance family of the capacity resource. </p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p> The specific EC2 instance type of the capacity resource. </p>"""
    instance_platform: NotRequired["capo_ec2.types.string.String"]
    """<p> The platform or operating system of the instance. </p>"""
    reservation_arn: NotRequired["capo_ec2.types.string.String"]
    """<p> The Amazon Resource Name (ARN) of the capacity reservation. This provides a unique identifier that can be used across Amazon Web Services services to reference the specific reservation. </p>"""
    reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The unique identifier of the capacity reservation. </p>"""
    reservation_type: NotRequired["capo_ec2.types.reservation_type.ReservationType"]
    """<p> The type of capacity reservation. </p>"""
    reservation_create_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the capacity reservation was originally created, in milliseconds since epoch. This differs from the start timestamp as reservations can be created before they become active. </p>"""
    reservation_start_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the capacity reservation becomes active and available for use, in milliseconds since epoch. This is when the reservation begins providing capacity. </p>"""
    reservation_end_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the capacity reservation expires and is no longer available, in milliseconds since epoch. After this time, the reservation will not provide any capacity. </p>"""
    reservation_end_date_type: NotRequired[
        "capo_ec2.types.reservation_end_date_type.ReservationEndDateType"
    ]
    """<p> The type of end date for the capacity reservation. This indicates whether the reservation has a fixed end date, is open-ended, or follows a specific termination pattern. </p>"""
    tenancy: NotRequired["capo_ec2.types.capacity_tenancy.CapacityTenancy"]
    """<p> The tenancy of the EC2 instances associated with this capacity dimension. Valid values are 'default' for shared tenancy, 'dedicated' for dedicated instances, or 'host' for dedicated hosts. </p>"""
    reservation_state: NotRequired["capo_ec2.types.reservation_state.ReservationState"]
    """<p> The current state of the capacity reservation. </p>"""
    reservation_instance_match_criteria: NotRequired["capo_ec2.types.string.String"]
    """<p> The instance matching criteria for the capacity reservation, determining how instances are matched to the reservation. </p>"""
    reservation_unused_financial_owner: NotRequired["capo_ec2.types.string.String"]
    """<p> The Amazon Web Services account ID that is financially responsible for unused capacity reservation costs. </p>"""
    tags: NotRequired[
        "capo_ec2.types.capacity_manager_tag_dimension_set.CapacityManagerTagDimensionSet"
    ]
    """<p> The tags associated with the capacity resource, represented as key-value pairs. Only tags that have been activated for monitoring via <code>UpdateCapacityManagerMonitoredTagKeys</code> are included. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerDimension, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_region" in value:
        pairs.append((f"{prefix}.ResourceRegion", str(value["resource_region"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "account_id" in value:
        pairs.append((f"{prefix}.AccountId", str(value["account_id"])))
    if "account_name" in value:
        pairs.append((f"{prefix}.AccountName", str(value["account_name"])))
    if "instance_family" in value:
        pairs.append((f"{prefix}.InstanceFamily", str(value["instance_family"])))
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "instance_platform" in value:
        pairs.append((f"{prefix}.InstancePlatform", str(value["instance_platform"])))
    if "reservation_arn" in value:
        pairs.append((f"{prefix}.ReservationArn", str(value["reservation_arn"])))
    if "reservation_id" in value:
        pairs.append((f"{prefix}.ReservationId", str(value["reservation_id"])))
    if "reservation_type" in value:
        import capo_ec2.types.reservation_type

        capo_ec2.types.reservation_type.serialize_ec2_query(
            value["reservation_type"], pairs, f"{prefix}.ReservationType"
        )
    if "reservation_create_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["reservation_create_timestamp"],
            pairs,
            f"{prefix}.ReservationCreateTimestamp",
        )
    if "reservation_start_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["reservation_start_timestamp"],
            pairs,
            f"{prefix}.ReservationStartTimestamp",
        )
    if "reservation_end_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["reservation_end_timestamp"],
            pairs,
            f"{prefix}.ReservationEndTimestamp",
        )
    if "reservation_end_date_type" in value:
        import capo_ec2.types.reservation_end_date_type

        capo_ec2.types.reservation_end_date_type.serialize_ec2_query(
            value["reservation_end_date_type"],
            pairs,
            f"{prefix}.ReservationEndDateType",
        )
    if "tenancy" in value:
        import capo_ec2.types.capacity_tenancy

        capo_ec2.types.capacity_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "reservation_state" in value:
        import capo_ec2.types.reservation_state

        capo_ec2.types.reservation_state.serialize_ec2_query(
            value["reservation_state"], pairs, f"{prefix}.ReservationState"
        )
    if "reservation_instance_match_criteria" in value:
        pairs.append(
            (
                f"{prefix}.ReservationInstanceMatchCriteria",
                str(value["reservation_instance_match_criteria"]),
            )
        )
    if "reservation_unused_financial_owner" in value:
        pairs.append(
            (
                f"{prefix}.ReservationUnusedFinancialOwner",
                str(value["reservation_unused_financial_owner"]),
            )
        )
    if "tags" in value:
        import capo_ec2.types.capacity_manager_tag_dimension_set

        capo_ec2.types.capacity_manager_tag_dimension_set.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerDimension:
    out: CapacityManagerDimension = {}  # type: ignore[typeddict-item]
    child_resource_region = el.find("ResourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_account_name = el.find("AccountName")
    if child_account_name is not None:
        out["account_name"] = str(child_account_name.text or "")
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_platform = el.find("InstancePlatform")
    if child_instance_platform is not None:
        out["instance_platform"] = str(child_instance_platform.text or "")
    child_reservation_arn = el.find("ReservationArn")
    if child_reservation_arn is not None:
        out["reservation_arn"] = str(child_reservation_arn.text or "")
    child_reservation_id = el.find("ReservationId")
    if child_reservation_id is not None:
        out["reservation_id"] = str(child_reservation_id.text or "")
    child_reservation_type = el.find("ReservationType")
    if child_reservation_type is not None:
        import capo_ec2.types.reservation_type

        out["reservation_type"] = capo_ec2.types.reservation_type.deserialize_ec2_query(
            child_reservation_type
        )
    child_reservation_create_timestamp = el.find("ReservationCreateTimestamp")
    if child_reservation_create_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["reservation_create_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_reservation_create_timestamp
            )
        )
    child_reservation_start_timestamp = el.find("ReservationStartTimestamp")
    if child_reservation_start_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["reservation_start_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_reservation_start_timestamp
            )
        )
    child_reservation_end_timestamp = el.find("ReservationEndTimestamp")
    if child_reservation_end_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["reservation_end_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_reservation_end_timestamp
            )
        )
    child_reservation_end_date_type = el.find("ReservationEndDateType")
    if child_reservation_end_date_type is not None:
        import capo_ec2.types.reservation_end_date_type

        out["reservation_end_date_type"] = (
            capo_ec2.types.reservation_end_date_type.deserialize_ec2_query(
                child_reservation_end_date_type
            )
        )
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.capacity_tenancy

        out["tenancy"] = capo_ec2.types.capacity_tenancy.deserialize_ec2_query(
            child_tenancy
        )
    child_reservation_state = el.find("ReservationState")
    if child_reservation_state is not None:
        import capo_ec2.types.reservation_state

        out["reservation_state"] = (
            capo_ec2.types.reservation_state.deserialize_ec2_query(
                child_reservation_state
            )
        )
    child_reservation_instance_match_criteria = el.find(
        "ReservationInstanceMatchCriteria"
    )
    if child_reservation_instance_match_criteria is not None:
        out["reservation_instance_match_criteria"] = str(
            child_reservation_instance_match_criteria.text or ""
        )
    child_reservation_unused_financial_owner = el.find(
        "ReservationUnusedFinancialOwner"
    )
    if child_reservation_unused_financial_owner is not None:
        out["reservation_unused_financial_owner"] = str(
            child_reservation_unused_financial_owner.text or ""
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.capacity_manager_tag_dimension_set

        out["tags"] = (
            capo_ec2.types.capacity_manager_tag_dimension_set.deserialize_ec2_query(
                el, "TagSet"
            )
        )
    return out
