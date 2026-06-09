"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4Pool``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.public_ipv4_pool_range_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class PublicIpv4Pool(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the address pool.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the address pool.</p>"""
    pool_address_ranges: NotRequired[
        "aws_sdk_ec2.types.public_ipv4_pool_range_set.PublicIpv4PoolRangeSet"
    ]
    """<p>The address ranges.</p>"""
    total_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of addresses.</p>"""
    total_available_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of available addresses.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the location from which the address pool is advertised. A network border group is a unique set of Availability Zones or Local Zones from where Amazon Web Services advertises public IP addresses.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags for the address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4Pool, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "pool_id" in value:
        pairs.append((f"{prefix}.PoolId", str(value["pool_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "pool_address_ranges" in value:
        import aws_sdk_ec2.types.public_ipv4_pool_range_set

        aws_sdk_ec2.types.public_ipv4_pool_range_set.serialize_ec2_query(
            value["pool_address_ranges"], pairs, f"{prefix}.PoolAddressRangeSet"
        )
    if "total_address_count" in value:
        pairs.append((f"{prefix}.TotalAddressCount", str(value["total_address_count"])))
    if "total_available_address_count" in value:
        pairs.append(
            (
                f"{prefix}.TotalAvailableAddressCount",
                str(value["total_available_address_count"]),
            )
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{prefix}.NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> PublicIpv4Pool:
    out: PublicIpv4Pool = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("PoolAddressRangeSet") is not None:
        import aws_sdk_ec2.types.public_ipv4_pool_range_set

        out["pool_address_ranges"] = (
            aws_sdk_ec2.types.public_ipv4_pool_range_set.deserialize_ec2_query(
                el, "PoolAddressRangeSet"
            )
        )
    child_total_address_count = el.find("TotalAddressCount")
    if child_total_address_count is not None:
        out["total_address_count"] = int(child_total_address_count.text or "")
    child_total_available_address_count = el.find("TotalAvailableAddressCount")
    if child_total_available_address_count is not None:
        out["total_available_address_count"] = int(
            child_total_available_address_count.text or ""
        )
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
