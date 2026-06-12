"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceCollection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instance_ids
    import aws_sdk_auto_scaling.types.xml_string_max_len64
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class InstanceCollection(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The instance type of the launched instances. </p>"""
    market_type: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p> The market type for the instances (On-Demand or Spot). </p>"""
    subnet_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The ID of the subnet where the instances were launched. </p>"""
    availability_zone: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The Availability Zone where the instances were launched. </p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The Availability Zone ID where the instances in this collection were launched. </p>"""
    instance_ids: NotRequired["aws_sdk_auto_scaling.types.instance_ids.InstanceIds"]
    """<p> A list of instance IDs for the successfully launched instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceCollection, pairs: list[tuple[str, str]], prefix: str
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
    if "instance_ids" in value:
        import aws_sdk_auto_scaling.types.instance_ids

        aws_sdk_auto_scaling.types.instance_ids.serialize_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )


def deserialize_query(el: Element) -> InstanceCollection:
    out: InstanceCollection = {}  # type: ignore[typeddict-item]
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
    child_instance_ids = el.find("InstanceIds")
    if child_instance_ids is not None:
        import aws_sdk_auto_scaling.types.instance_ids

        out["instance_ids"] = aws_sdk_auto_scaling.types.instance_ids.deserialize_query(
            child_instance_ids
        )
    return out
