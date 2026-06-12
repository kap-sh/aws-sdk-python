"""Generated from Smithy shape ``com.amazonaws.redshift#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.tag

TagList: TypeAlias = list["aws_sdk_redshift.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(value: TagList, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_redshift.types.tag

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.tag.serialize_query(item, pairs, f"{prefix}.Tag.{n}")


def deserialize_query(el: Element) -> TagList:
    import aws_sdk_redshift.types.tag

    out: TagList = []
    for child in el.findall("Tag"):
        out.append(aws_sdk_redshift.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.tag

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TagList:
    import aws_sdk_redshift.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.tag.deserialize_query(child))
    return out
