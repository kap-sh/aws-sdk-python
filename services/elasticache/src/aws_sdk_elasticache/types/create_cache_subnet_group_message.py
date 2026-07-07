"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.subnet_identifier_list
    import aws_sdk_elasticache.types.tag_list


class CreateCacheSubnetGroupMessage(TypedDict, closed=True):
    cache_subnet_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>A name for the cache subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters or hyphens.</p> <p>Example: <code>mysubnetgroup</code> </p>"""
    cache_subnet_group_description: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>A description for the cache subnet group.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_elasticache.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>A list of VPC subnet IDs for the cache subnet group.</p>"""
    tags: NotRequired["aws_sdk_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCacheSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_subnet_group_name" in value:
        pairs.append(
            (f"{prefix}.CacheSubnetGroupName", str(value["cache_subnet_group_name"]))
        )
    if "cache_subnet_group_description" in value:
        pairs.append(
            (
                f"{prefix}.CacheSubnetGroupDescription",
                str(value["cache_subnet_group_description"]),
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_elasticache.types.subnet_identifier_list

        aws_sdk_elasticache.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "tags" in value:
        import aws_sdk_elasticache.types.tag_list

        aws_sdk_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateCacheSubnetGroupMessage:
    out: CreateCacheSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_subnet_group_name = el.find("CacheSubnetGroupName")
    if child_cache_subnet_group_name is not None:
        out["cache_subnet_group_name"] = str(child_cache_subnet_group_name.text or "")
    child_cache_subnet_group_description = el.find("CacheSubnetGroupDescription")
    if child_cache_subnet_group_description is not None:
        out["cache_subnet_group_description"] = str(
            child_cache_subnet_group_description.text or ""
        )
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import aws_sdk_elasticache.types.subnet_identifier_list

        out["subnet_ids"] = (
            aws_sdk_elasticache.types.subnet_identifier_list.deserialize_query(
                child_subnet_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elasticache.types.tag_list

        out["tags"] = aws_sdk_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
