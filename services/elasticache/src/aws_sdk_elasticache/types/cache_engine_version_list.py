"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheEngineVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_engine_version

CacheEngineVersionList: TypeAlias = list[
    "aws_sdk_elasticache.types.cache_engine_version.CacheEngineVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheEngineVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_engine_version

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_engine_version.serialize_query(
            item, pairs, f"{prefix}.CacheEngineVersion.{n}"
        )


def deserialize_query(el: Element) -> CacheEngineVersionList:
    import aws_sdk_elasticache.types.cache_engine_version

    out: CacheEngineVersionList = []
    for child in el.findall("CacheEngineVersion"):
        out.append(
            aws_sdk_elasticache.types.cache_engine_version.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CacheEngineVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_engine_version

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_engine_version.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheEngineVersionList:
    import aws_sdk_elasticache.types.cache_engine_version

    out: CacheEngineVersionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.cache_engine_version.deserialize_query(child)
        )
    return out
