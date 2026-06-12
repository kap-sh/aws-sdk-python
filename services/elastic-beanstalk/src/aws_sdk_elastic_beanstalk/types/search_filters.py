"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SearchFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.search_filter

SearchFilters: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.search_filter.SearchFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SearchFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.search_filter

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.search_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SearchFilters:
    import aws_sdk_elastic_beanstalk.types.search_filter

    out: SearchFilters = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.search_filter.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: SearchFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.search_filter

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.search_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SearchFilters:
    import aws_sdk_elastic_beanstalk.types.search_filter

    out: SearchFilters = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.search_filter.deserialize_query(child)
        )
    return out
