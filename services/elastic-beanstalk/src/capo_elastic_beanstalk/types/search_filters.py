"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SearchFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.search_filter

SearchFilters: TypeAlias = list[
    "capo_elastic_beanstalk.types.search_filter.SearchFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SearchFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.search_filter

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.search_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SearchFilters:
    import capo_elastic_beanstalk.types.search_filter

    out: SearchFilters = []
    for child in el.findall("member"):
        out.append(capo_elastic_beanstalk.types.search_filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SearchFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.search_filter

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.search_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SearchFilters:
    import capo_elastic_beanstalk.types.search_filter

    out: SearchFilters = []
    for child in parent.findall(tag):
        out.append(capo_elastic_beanstalk.types.search_filter.deserialize_query(child))
    return out
