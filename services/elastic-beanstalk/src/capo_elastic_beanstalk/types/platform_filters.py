"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_filter

PlatformFilters: TypeAlias = list[
    "capo_elastic_beanstalk.types.platform_filter.PlatformFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.platform_filter

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.platform_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PlatformFilters:
    import capo_elastic_beanstalk.types.platform_filter

    out: PlatformFilters = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.platform_filter.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PlatformFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.platform_filter

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.platform_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PlatformFilters:
    import capo_elastic_beanstalk.types.platform_filter

    out: PlatformFilters = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.platform_filter.deserialize_query(child)
        )
    return out
