"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6Pool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.pool_cidr_blocks_set
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class Ipv6Pool(TypedDict, closed=True):
    pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the address pool.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the address pool.</p>"""
    pool_cidr_blocks: NotRequired[
        "capo_ec2.types.pool_cidr_blocks_set.PoolCidrBlocksSet"
    ]
    """<p>The CIDR blocks for the address pool.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags for the address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6Pool, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "pool_cidr_blocks" in value:
        import capo_ec2.types.pool_cidr_blocks_set

        capo_ec2.types.pool_cidr_blocks_set.serialize_ec2_query(
            value["pool_cidr_blocks"], pairs, f"{key_prefix}PoolCidrBlockSet"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> Ipv6Pool:
    out: Ipv6Pool = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("poolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_pool_cidr_blocks = el.find("poolCidrBlockSet")
    if child_pool_cidr_blocks is not None:
        import capo_ec2.types.pool_cidr_blocks_set

        out["pool_cidr_blocks"] = (
            capo_ec2.types.pool_cidr_blocks_set.deserialize_ec2_query(
                child_pool_cidr_blocks
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
