"""Generated from Smithy shape ``com.amazonaws.autoscaling#LifecycleHooks``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.lifecycle_hook

LifecycleHooks: TypeAlias = list["capo_auto_scaling.types.lifecycle_hook.LifecycleHook"]


# --- awsQuery ser/de ---
def serialize_query(
    value: LifecycleHooks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.lifecycle_hook

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.lifecycle_hook.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LifecycleHooks:
    import capo_auto_scaling.types.lifecycle_hook

    out: LifecycleHooks = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.lifecycle_hook.deserialize_query(child))
    return out


def serialize_query_flat(
    value: LifecycleHooks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.lifecycle_hook

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.lifecycle_hook.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LifecycleHooks:
    import capo_auto_scaling.types.lifecycle_hook

    out: LifecycleHooks = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.lifecycle_hook.deserialize_query(child))
    return out
