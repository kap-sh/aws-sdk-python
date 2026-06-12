"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceGenerations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instance_generation

InstanceGenerations: TypeAlias = list[
    "aws_sdk_auto_scaling.types.instance_generation.InstanceGeneration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceGenerations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.instance_generation

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.instance_generation.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstanceGenerations:
    import aws_sdk_auto_scaling.types.instance_generation

    out: InstanceGenerations = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.instance_generation.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: InstanceGenerations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.instance_generation

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.instance_generation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstanceGenerations:
    import aws_sdk_auto_scaling.types.instance_generation

    out: InstanceGenerations = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.instance_generation.deserialize_query(child)
        )
    return out
