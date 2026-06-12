"""Generated from Smithy shape ``com.amazonaws.autoscaling#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.filter

Filters: TypeAlias = list["aws_sdk_auto_scaling.types.filter.Filter"]


# --- awsQuery ser/de ---
def serialize_query(value: Filters, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_auto_scaling.types.filter

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Filters:
    import aws_sdk_auto_scaling.types.filter

    out: Filters = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Filters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.filter

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.filter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Filters:
    import aws_sdk_auto_scaling.types.filter

    out: Filters = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.filter.deserialize_query(child))
    return out
