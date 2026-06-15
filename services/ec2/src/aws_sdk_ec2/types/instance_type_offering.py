"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.location
    import aws_sdk_ec2.types.location_type


class InstanceTypeOffering(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    r"""<p>The instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    location_type: NotRequired["aws_sdk_ec2.types.location_type.LocationType"]
    """<p>The location type.</p>"""
    location: NotRequired["aws_sdk_ec2.types.location.Location"]
    """<p>The identifier for the location. This depends on the location type. For example, if the location type is <code>region</code>, the location is the Region code (for example, <code>us-east-2</code>.)</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "location_type" in value:
        import aws_sdk_ec2.types.location_type

        aws_sdk_ec2.types.location_type.serialize_ec2_query(
            value["location_type"], pairs, f"{prefix}.LocationType"
        )
    if "location" in value:
        pairs.append((f"{prefix}.Location", str(value["location"])))


def deserialize_ec2_query(el: Element) -> InstanceTypeOffering:
    out: InstanceTypeOffering = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_location_type = el.find("LocationType")
    if child_location_type is not None:
        import aws_sdk_ec2.types.location_type

        out["location_type"] = aws_sdk_ec2.types.location_type.deserialize_ec2_query(
            child_location_type
        )
    child_location = el.find("Location")
    if child_location is not None:
        out["location"] = str(child_location.text or "")
    return out
