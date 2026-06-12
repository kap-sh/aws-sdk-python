"""Generated from Smithy shape ``com.amazonaws.elasticache#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.filter

FilterList: TypeAlias = list["aws_sdk_elasticache.types.filter.Filter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.filter

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> FilterList:
    import aws_sdk_elasticache.types.filter

    out: FilterList = []
    for child in el.findall("member"):
        out.append(aws_sdk_elasticache.types.filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: FilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.filter

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.filter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> FilterList:
    import aws_sdk_elasticache.types.filter

    out: FilterList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.filter.deserialize_query(child))
    return out
