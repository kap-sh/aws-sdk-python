"""Generated from Smithy shape ``com.amazonaws.autoscaling#Activities``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.activity

Activities: TypeAlias = list["aws_sdk_auto_scaling.types.activity.Activity"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Activities, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.activity

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.activity.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Activities:
    import aws_sdk_auto_scaling.types.activity

    out: Activities = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.activity.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Activities, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.activity

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.activity.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Activities:
    import aws_sdk_auto_scaling.types.activity

    out: Activities = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.activity.deserialize_query(child))
    return out
