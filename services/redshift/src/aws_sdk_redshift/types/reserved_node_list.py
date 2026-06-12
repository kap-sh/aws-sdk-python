"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.reserved_node

ReservedNodeList: TypeAlias = list["aws_sdk_redshift.types.reserved_node.ReservedNode"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.reserved_node

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.reserved_node.serialize_query(
            item, pairs, f"{prefix}.ReservedNode.{n}"
        )


def deserialize_query(el: Element) -> ReservedNodeList:
    import aws_sdk_redshift.types.reserved_node

    out: ReservedNodeList = []
    for child in el.findall("ReservedNode"):
        out.append(aws_sdk_redshift.types.reserved_node.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReservedNodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.reserved_node

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.reserved_node.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReservedNodeList:
    import aws_sdk_redshift.types.reserved_node

    out: ReservedNodeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.reserved_node.deserialize_query(child))
    return out
