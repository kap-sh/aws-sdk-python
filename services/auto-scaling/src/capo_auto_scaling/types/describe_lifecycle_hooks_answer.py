"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeLifecycleHooksAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.lifecycle_hooks


class DescribeLifecycleHooksAnswer(TypedDict, closed=True):
    lifecycle_hooks: NotRequired[
        "capo_auto_scaling.types.lifecycle_hooks.LifecycleHooks"
    ]
    """<p>The lifecycle hooks for the specified group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLifecycleHooksAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "lifecycle_hooks" in value:
        import capo_auto_scaling.types.lifecycle_hooks

        capo_auto_scaling.types.lifecycle_hooks.serialize_query(
            value["lifecycle_hooks"], pairs, f"{key_prefix}LifecycleHooks"
        )


def deserialize_query(el: Element) -> DescribeLifecycleHooksAnswer:
    out: DescribeLifecycleHooksAnswer = {}  # type: ignore[typeddict-item]
    child_lifecycle_hooks = el.find("LifecycleHooks")
    if child_lifecycle_hooks is not None:
        import capo_auto_scaling.types.lifecycle_hooks

        out["lifecycle_hooks"] = (
            capo_auto_scaling.types.lifecycle_hooks.deserialize_query(
                child_lifecycle_hooks
            )
        )
    return out
