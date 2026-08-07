"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyCacheSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.subnet_identifier_list


class ModifyCacheSubnetGroupMessage(TypedDict, closed=True):
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name for the cache subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters or hyphens.</p> <p>Example: <code>mysubnetgroup</code> </p>"""
    cache_subnet_group_description: NotRequired["capo_elasticache.types.string.String"]
    """<p>A description of the cache subnet group.</p>"""
    subnet_ids: NotRequired[
        "capo_elasticache.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>The EC2 subnet IDs for the cache subnet group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCacheSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}CacheSubnetGroupName", str(value["cache_subnet_group_name"]))
        )
    if "cache_subnet_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}CacheSubnetGroupDescription",
                str(value["cache_subnet_group_description"]),
            )
        )
    if "subnet_ids" in value:
        import capo_elasticache.types.subnet_identifier_list

        capo_elasticache.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIds"
        )


def deserialize_query(el: Element) -> ModifyCacheSubnetGroupMessage:
    out: ModifyCacheSubnetGroupMessage = {}  # type: ignore[typeddict-item]
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
        import capo_elasticache.types.subnet_identifier_list

        out["subnet_ids"] = (
            capo_elasticache.types.subnet_identifier_list.deserialize_query(
                child_subnet_ids
            )
        )
    return out
