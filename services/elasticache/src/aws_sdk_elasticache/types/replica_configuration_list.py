"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicaConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.configure_shard

ReplicaConfigurationList: TypeAlias = list[
    "aws_sdk_elasticache.types.configure_shard.ConfigureShard"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicaConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.configure_shard

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.configure_shard.serialize_query(
            item, pairs, f"{prefix}.ConfigureShard.{n}"
        )


def deserialize_query(el: Element) -> ReplicaConfigurationList:
    import aws_sdk_elasticache.types.configure_shard

    out: ReplicaConfigurationList = []
    for child in el.findall("ConfigureShard"):
        out.append(aws_sdk_elasticache.types.configure_shard.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReplicaConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.configure_shard

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.configure_shard.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReplicaConfigurationList:
    import aws_sdk_elasticache.types.configure_shard

    out: ReplicaConfigurationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.configure_shard.deserialize_query(child))
    return out
