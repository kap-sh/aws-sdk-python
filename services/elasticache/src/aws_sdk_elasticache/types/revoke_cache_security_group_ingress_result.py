"""Generated from Smithy shape ``com.amazonaws.elasticache#RevokeCacheSecurityGroupIngressResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_security_group


class RevokeCacheSecurityGroupIngressResult(TypedDict):
    cache_security_group: NotRequired[
        "aws_sdk_elasticache.types.cache_security_group.CacheSecurityGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeCacheSecurityGroupIngressResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cache_security_group" in value:
        import aws_sdk_elasticache.types.cache_security_group

        aws_sdk_elasticache.types.cache_security_group.serialize_query(
            value["cache_security_group"], pairs, f"{prefix}.CacheSecurityGroup"
        )


def deserialize_query(el: Element) -> RevokeCacheSecurityGroupIngressResult:
    out: RevokeCacheSecurityGroupIngressResult = {}  # type: ignore[typeddict-item]
    child_cache_security_group = el.find("CacheSecurityGroup")
    if child_cache_security_group is not None:
        import aws_sdk_elasticache.types.cache_security_group

        out["cache_security_group"] = (
            aws_sdk_elasticache.types.cache_security_group.deserialize_query(
                child_cache_security_group
            )
        )
    return out
