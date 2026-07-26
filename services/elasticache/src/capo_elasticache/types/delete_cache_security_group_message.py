"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class DeleteCacheSecurityGroupMessage(TypedDict, closed=True):
    cache_security_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache security group to delete.</p> <note> <p>You cannot delete the default security group.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheSecurityGroupName",
                str(value["cache_security_group_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteCacheSecurityGroupMessage:
    out: DeleteCacheSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_security_group_name = el.find("CacheSecurityGroupName")
    if child_cache_security_group_name is not None:
        out["cache_security_group_name"] = str(
            child_cache_security_group_name.text or ""
        )
    return out
