"""Generated from Smithy shape ``com.amazonaws.sts#tagListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.tag

tagListType: TypeAlias = list["aws_sdk_sts.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(
    value: tagListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sts.types.tag

    for n, item in enumerate(value, 1):
        aws_sdk_sts.types.tag.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> tagListType:
    import aws_sdk_sts.types.tag

    out: tagListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_sts.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: tagListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sts.types.tag

    for n, item in enumerate(value, 1):
        aws_sdk_sts.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> tagListType:
    import aws_sdk_sts.types.tag

    out: tagListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sts.types.tag.deserialize_query(child))
    return out
