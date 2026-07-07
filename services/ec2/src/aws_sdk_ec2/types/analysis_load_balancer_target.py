"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisLoadBalancerTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_component
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.port
    import aws_sdk_ec2.types.string


class AnalysisLoadBalancerTarget(TypedDict, closed=True):
    address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    instance: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>Information about the instance.</p>"""
    port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The port on which the target is listening.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisLoadBalancerTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance" in value:
        import aws_sdk_ec2.types.analysis_component

        aws_sdk_ec2.types.analysis_component.serialize_ec2_query(
            value["instance"], pairs, f"{prefix}.Instance"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))


def deserialize_ec2_query(el: Element) -> AnalysisLoadBalancerTarget:
    out: AnalysisLoadBalancerTarget = {}  # type: ignore[typeddict-item]
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance = el.find("Instance")
    if child_instance is not None:
        import aws_sdk_ec2.types.analysis_component

        out["instance"] = aws_sdk_ec2.types.analysis_component.deserialize_ec2_query(
            child_instance
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    return out
