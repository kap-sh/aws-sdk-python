"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchInstancesError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string
    import aws_sdk_auto_scaling.types.xml_string_max_len64
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class LaunchInstancesError(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The instance type that failed to launch. </p>"""
    market_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p> The market type (On-Demand or Spot) that encountered the launch error. </p>"""
    subnet_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The subnet ID where the instance launch was attempted. </p>"""
    availability_zone: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The Availability Zone where the instance launch was attempted. </p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The Availability Zone ID where the launch error occurred. </p>"""
    error_code: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p> The error code representing the type of error encountered (e.g., InsufficientInstanceCapacity). </p>"""
    error_message: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p> A descriptive message providing details about the error encountered during the launch attempt. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchInstancesError, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "market_type" in value:
        pairs.append((f"{prefix}.MarketType", str(value["market_type"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "error_code" in value:
        pairs.append((f"{prefix}.ErrorCode", str(value["error_code"])))
    if "error_message" in value:
        pairs.append((f"{prefix}.ErrorMessage", str(value["error_message"])))


def deserialize_query(el: Element) -> LaunchInstancesError:
    out: LaunchInstancesError = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_market_type = el.find("MarketType")
    if child_market_type is not None:
        out["market_type"] = str(child_market_type.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_error_code = el.find("ErrorCode")
    if child_error_code is not None:
        out["error_code"] = str(child_error_code.text or "")
    child_error_message = el.find("ErrorMessage")
    if child_error_message is not None:
        out["error_message"] = str(child_error_message.text or "")
    return out
