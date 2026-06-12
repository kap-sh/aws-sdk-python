"""Generated from Smithy shape ``com.amazonaws.neptune#RangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.range

RangeList: TypeAlias = list["aws_sdk_neptune.types.range.Range"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.range

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.range.serialize_query(item, pairs, f"{prefix}.Range.{n}")


def deserialize_query(el: Element) -> RangeList:
    import aws_sdk_neptune.types.range

    out: RangeList = []
    for child in el.findall("Range"):
        out.append(aws_sdk_neptune.types.range.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.range

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.range.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> RangeList:
    import aws_sdk_neptune.types.range

    out: RangeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_neptune.types.range.deserialize_query(child))
    return out
