"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPrice``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.ri_product_description
    import aws_sdk_ec2.types.string


class SpotPrice(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    product_description: NotRequired[
        "aws_sdk_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>A general description of the AMI.</p>"""
    spot_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the request was created, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotPrice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "product_description" in value:
        import aws_sdk_ec2.types.ri_product_description

        aws_sdk_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{prefix}.ProductDescription"
        )
    if "spot_price" in value:
        pairs.append((f"{prefix}.SpotPrice", str(value["spot_price"])))
    if "timestamp" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )


def deserialize_ec2_query(el: Element) -> SpotPrice:
    out: SpotPrice = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        import aws_sdk_ec2.types.ri_product_description

        out["product_description"] = (
            aws_sdk_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    child_spot_price = el.find("SpotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_ec2.types.date_time

        out["timestamp"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_timestamp
        )
    return out
