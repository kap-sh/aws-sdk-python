"""Generated from Smithy shape ``com.amazonaws.elasticache#NetworkTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.network_type

NetworkTypeList: TypeAlias = list["aws_sdk_elasticache.types.network_type.NetworkType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.network_type

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.network_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> NetworkTypeList:
    import aws_sdk_elasticache.types.network_type

    out: NetworkTypeList = []
    for child in el.findall("member"):
        out.append(aws_sdk_elasticache.types.network_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NetworkTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.network_type

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.network_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NetworkTypeList:
    import aws_sdk_elasticache.types.network_type

    out: NetworkTypeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.network_type.deserialize_query(child))
    return out
