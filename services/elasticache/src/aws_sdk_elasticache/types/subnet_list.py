"""Generated from Smithy shape ``com.amazonaws.elasticache#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.subnet

SubnetList: TypeAlias = list["aws_sdk_elasticache.types.subnet.Subnet"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.subnet

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.subnet.serialize_query(
            item, pairs, f"{prefix}.Subnet.{n}"
        )


def deserialize_query(el: Element) -> SubnetList:
    import aws_sdk_elasticache.types.subnet

    out: SubnetList = []
    for child in el.findall("Subnet"):
        out.append(aws_sdk_elasticache.types.subnet.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.subnet

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.subnet.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SubnetList:
    import aws_sdk_elasticache.types.subnet

    out: SubnetList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.subnet.deserialize_query(child))
    return out
