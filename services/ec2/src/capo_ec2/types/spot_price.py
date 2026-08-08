"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPrice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_type
    import capo_ec2.types.ri_product_description
    import capo_ec2.types.string


class SpotPrice(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    product_description: NotRequired[
        "capo_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>A general description of the AMI.</p>"""
    spot_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    timestamp: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time the request was created, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotPrice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "product_description" in value:
        import capo_ec2.types.ri_product_description

        capo_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{key_prefix}ProductDescription"
        )
    if "spot_price" in value:
        pairs.append((f"{key_prefix}SpotPrice", str(value["spot_price"])))
    if "timestamp" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )


def deserialize_ec2_query(el: Element) -> SpotPrice:
    out: SpotPrice = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_product_description = el.find("productDescription")
    if child_product_description is not None:
        import capo_ec2.types.ri_product_description

        out["product_description"] = (
            capo_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    child_spot_price = el.find("spotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_timestamp = el.find("timestamp")
    if child_timestamp is not None:
        import capo_ec2.types.date_time

        out["timestamp"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_timestamp
        )
    return out
