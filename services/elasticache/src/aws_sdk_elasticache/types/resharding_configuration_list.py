"""Generated from Smithy shape ``com.amazonaws.elasticache#ReshardingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.resharding_configuration

ReshardingConfigurationList: TypeAlias = list[
    "aws_sdk_elasticache.types.resharding_configuration.ReshardingConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReshardingConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.resharding_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.resharding_configuration.serialize_query(
            item, pairs, f"{prefix}.ReshardingConfiguration.{n}"
        )


def deserialize_query(el: Element) -> ReshardingConfigurationList:
    import aws_sdk_elasticache.types.resharding_configuration

    out: ReshardingConfigurationList = []
    for child in el.findall("ReshardingConfiguration"):
        out.append(
            aws_sdk_elasticache.types.resharding_configuration.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ReshardingConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.resharding_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.resharding_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReshardingConfigurationList:
    import aws_sdk_elasticache.types.resharding_configuration

    out: ReshardingConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.resharding_configuration.deserialize_query(child)
        )
    return out
