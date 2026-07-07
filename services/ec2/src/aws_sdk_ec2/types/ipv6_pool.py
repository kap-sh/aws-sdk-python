"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6Pool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.pool_cidr_blocks_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class Ipv6Pool(TypedDict, closed=True):
    pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the address pool.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the address pool.</p>"""
    pool_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.pool_cidr_blocks_set.PoolCidrBlocksSet"
    ]
    """<p>The CIDR blocks for the address pool.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags for the address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6Pool, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "pool_id" in value:
        pairs.append((f"{prefix}.PoolId", str(value["pool_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "pool_cidr_blocks" in value:
        import aws_sdk_ec2.types.pool_cidr_blocks_set

        aws_sdk_ec2.types.pool_cidr_blocks_set.serialize_ec2_query(
            value["pool_cidr_blocks"], pairs, f"{prefix}.PoolCidrBlockSet"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> Ipv6Pool:
    out: Ipv6Pool = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("PoolCidrBlockSet") is not None:
        import aws_sdk_ec2.types.pool_cidr_blocks_set

        out["pool_cidr_blocks"] = (
            aws_sdk_ec2.types.pool_cidr_blocks_set.deserialize_ec2_query(
                el, "PoolCidrBlockSet"
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
