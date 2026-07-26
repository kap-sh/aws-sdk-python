"""Generated from Smithy shape ``com.amazonaws.elasticache#RegionalConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.regional_configuration

RegionalConfigurationList: TypeAlias = list[
    "capo_elasticache.types.regional_configuration.RegionalConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionalConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.regional_configuration

    for n, item in enumerate(value, 1):
        capo_elasticache.types.regional_configuration.serialize_query(
            item, pairs, f"{prefix}.RegionalConfiguration.{n}"
        )


def deserialize_query(el: Element) -> RegionalConfigurationList:
    import capo_elasticache.types.regional_configuration

    out: RegionalConfigurationList = []
    for child in el.findall("RegionalConfiguration"):
        out.append(
            capo_elasticache.types.regional_configuration.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RegionalConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.regional_configuration

    for n, item in enumerate(value, 1):
        capo_elasticache.types.regional_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RegionalConfigurationList:
    import capo_elasticache.types.regional_configuration

    out: RegionalConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.regional_configuration.deserialize_query(child)
        )
    return out
