"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.availability_zone_ids_limit1
    import aws_sdk_auto_scaling.types.availability_zones_limit1
    import aws_sdk_auto_scaling.types.client_token
    import aws_sdk_auto_scaling.types.requested_capacity
    import aws_sdk_auto_scaling.types.retry_strategy
    import aws_sdk_auto_scaling.types.subnet_ids_limit1
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class LaunchInstancesRequest(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The name of the Auto Scaling group to launch instances into. </p>"""
    requested_capacity: NotRequired[
        "aws_sdk_auto_scaling.types.requested_capacity.RequestedCapacity"
    ]
    """<p> The number of instances to launch. Although this value can exceed 100 for instance weights, the actual instance count is limited to 100 instances per launch. </p>"""
    client_token: NotRequired["aws_sdk_auto_scaling.types.client_token.ClientToken"]
    """<p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>"""
    availability_zones: NotRequired[
        "aws_sdk_auto_scaling.types.availability_zones_limit1.AvailabilityZonesLimit1"
    ]
    """<p> The Availability Zones for the instance launch. Must match or be included in the Auto Scaling group's Availability Zone configuration. Either <code>AvailabilityZones</code> or <code>SubnetIds</code> must be specified for groups with multiple Availability Zone configurations. </p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_auto_scaling.types.availability_zone_ids_limit1.AvailabilityZoneIdsLimit1"
    ]
    """<p> A list of Availability Zone IDs where instances should be launched. Must match or be included in the group's AZ configuration. You cannot specify both AvailabilityZones and AvailabilityZoneIds. Required for multi-AZ groups, optional for single-AZ groups. </p>"""
    subnet_ids: NotRequired[
        "aws_sdk_auto_scaling.types.subnet_ids_limit1.SubnetIdsLimit1"
    ]
    """<p> The subnet IDs for the instance launch. Either <code>AvailabilityZones</code> or <code>SubnetIds</code> must be specified. If both are specified, the subnets must reside in the specified Availability Zones. </p>"""
    retry_strategy: NotRequired[
        "aws_sdk_auto_scaling.types.retry_strategy.RetryStrategy"
    ]
    """<p> Specifies whether to retry asynchronously if the synchronous launch fails. Valid values are NONE (default, no async retry) and RETRY_WITH_GROUP_CONFIGURATION (increase desired capacity and retry with group configuration). </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "requested_capacity" in value:
        pairs.append((f"{prefix}.RequestedCapacity", str(value["requested_capacity"])))
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "availability_zones" in value:
        import aws_sdk_auto_scaling.types.availability_zones_limit1

        aws_sdk_auto_scaling.types.availability_zones_limit1.serialize_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )
    if "availability_zone_ids" in value:
        import aws_sdk_auto_scaling.types.availability_zone_ids_limit1

        aws_sdk_auto_scaling.types.availability_zone_ids_limit1.serialize_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIds"
        )
    if "subnet_ids" in value:
        import aws_sdk_auto_scaling.types.subnet_ids_limit1

        aws_sdk_auto_scaling.types.subnet_ids_limit1.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "retry_strategy" in value:
        import aws_sdk_auto_scaling.types.retry_strategy

        aws_sdk_auto_scaling.types.retry_strategy.serialize_query(
            value["retry_strategy"], pairs, f"{prefix}.RetryStrategy"
        )


def deserialize_query(el: Element) -> LaunchInstancesRequest:
    out: LaunchInstancesRequest = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_requested_capacity = el.find("RequestedCapacity")
    if child_requested_capacity is not None:
        out["requested_capacity"] = int(child_requested_capacity.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import aws_sdk_auto_scaling.types.availability_zones_limit1

        out["availability_zones"] = (
            aws_sdk_auto_scaling.types.availability_zones_limit1.deserialize_query(
                child_availability_zones
            )
        )
    child_availability_zone_ids = el.find("AvailabilityZoneIds")
    if child_availability_zone_ids is not None:
        import aws_sdk_auto_scaling.types.availability_zone_ids_limit1

        out["availability_zone_ids"] = (
            aws_sdk_auto_scaling.types.availability_zone_ids_limit1.deserialize_query(
                child_availability_zone_ids
            )
        )
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import aws_sdk_auto_scaling.types.subnet_ids_limit1

        out["subnet_ids"] = (
            aws_sdk_auto_scaling.types.subnet_ids_limit1.deserialize_query(
                child_subnet_ids
            )
        )
    child_retry_strategy = el.find("RetryStrategy")
    if child_retry_strategy is not None:
        import aws_sdk_auto_scaling.types.retry_strategy

        out["retry_strategy"] = (
            aws_sdk_auto_scaling.types.retry_strategy.deserialize_query(
                child_retry_strategy
            )
        )
    return out
