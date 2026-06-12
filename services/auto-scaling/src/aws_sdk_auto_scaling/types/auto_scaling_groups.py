"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.auto_scaling_group

AutoScalingGroups: TypeAlias = list[
    "aws_sdk_auto_scaling.types.auto_scaling_group.AutoScalingGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.auto_scaling_group

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.auto_scaling_group.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AutoScalingGroups:
    import aws_sdk_auto_scaling.types.auto_scaling_group

    out: AutoScalingGroups = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.auto_scaling_group.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AutoScalingGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.auto_scaling_group

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.auto_scaling_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AutoScalingGroups:
    import aws_sdk_auto_scaling.types.auto_scaling_group

    out: AutoScalingGroups = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.auto_scaling_group.deserialize_query(child)
        )
    return out
