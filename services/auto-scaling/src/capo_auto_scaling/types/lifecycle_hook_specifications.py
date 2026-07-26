"""Generated from Smithy shape ``com.amazonaws.autoscaling#LifecycleHookSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.lifecycle_hook_specification

LifecycleHookSpecifications: TypeAlias = list[
    "capo_auto_scaling.types.lifecycle_hook_specification.LifecycleHookSpecification"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LifecycleHookSpecifications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.lifecycle_hook_specification

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.lifecycle_hook_specification.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LifecycleHookSpecifications:
    import capo_auto_scaling.types.lifecycle_hook_specification

    out: LifecycleHookSpecifications = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.lifecycle_hook_specification.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LifecycleHookSpecifications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.lifecycle_hook_specification

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.lifecycle_hook_specification.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LifecycleHookSpecifications:
    import capo_auto_scaling.types.lifecycle_hook_specification

    out: LifecycleHookSpecifications = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.lifecycle_hook_specification.deserialize_query(
                child
            )
        )
    return out
