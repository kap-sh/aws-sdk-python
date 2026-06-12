"""Generated from Smithy shape ``com.amazonaws.rds#TagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.tag_specification

TagSpecificationList: TypeAlias = list[
    "aws_sdk_rds.types.tag_specification.TagSpecification"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.tag_specification

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.tag_specification.serialize_query(
            item, pairs, f"{prefix}.item.{n}"
        )


def deserialize_query(el: Element) -> TagSpecificationList:
    import aws_sdk_rds.types.tag_specification

    out: TagSpecificationList = []
    for child in el.findall("item"):
        out.append(aws_sdk_rds.types.tag_specification.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.tag_specification

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.tag_specification.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TagSpecificationList:
    import aws_sdk_rds.types.tag_specification

    out: TagSpecificationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.tag_specification.deserialize_query(child))
    return out
