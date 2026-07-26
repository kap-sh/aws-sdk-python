"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingInstances``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_instance_details

AutoScalingInstances: TypeAlias = list[
    "capo_auto_scaling.types.auto_scaling_instance_details.AutoScalingInstanceDetails"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.auto_scaling_instance_details

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.auto_scaling_instance_details.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AutoScalingInstances:
    import capo_auto_scaling.types.auto_scaling_instance_details

    out: AutoScalingInstances = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.auto_scaling_instance_details.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AutoScalingInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.auto_scaling_instance_details

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.auto_scaling_instance_details.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AutoScalingInstances:
    import capo_auto_scaling.types.auto_scaling_instance_details

    out: AutoScalingInstances = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.auto_scaling_instance_details.deserialize_query(
                child
            )
        )
    return out
