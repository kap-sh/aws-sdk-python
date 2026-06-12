"""Generated from Smithy shape ``com.amazonaws.autoscaling#Instances``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instance

Instances: TypeAlias = list["aws_sdk_auto_scaling.types.instance.Instance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Instances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.instance

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.instance.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Instances:
    import aws_sdk_auto_scaling.types.instance

    out: Instances = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.instance.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Instances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.instance

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.instance.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Instances:
    import aws_sdk_auto_scaling.types.instance

    out: Instances = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.instance.deserialize_query(child))
    return out
