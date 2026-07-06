"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scope
    import aws_sdk_ec2.types.string


class ReservedInstancesConfiguration(TypedDict, closed=True):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the modified Reserved Instances.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of modified Reserved Instances.</p> <note> <p>This is a required field for a request.</p> </note>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type for the modified Reserved Instances.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network platform of the modified Reserved Instances.</p>"""
    scope: NotRequired["aws_sdk_ec2.types.scope.scope"]
    """<p>Whether the Reserved Instance is applied to instances in a Region or instances in a specific Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "platform" in value:
        pairs.append((f"{prefix}.Platform", str(value["platform"])))
    if "scope" in value:
        import aws_sdk_ec2.types.scope

        aws_sdk_ec2.types.scope.serialize_ec2_query(
            value["scope"], pairs, f"{prefix}.Scope"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesConfiguration:
    out: ReservedInstancesConfiguration = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    child_scope = el.find("Scope")
    if child_scope is not None:
        import aws_sdk_ec2.types.scope

        out["scope"] = aws_sdk_ec2.types.scope.deserialize_ec2_query(child_scope)
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
