"""Generated from Smithy shape ``com.amazonaws.autoscaling#Overrides``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.launch_template_overrides

Overrides: TypeAlias = list[
    "capo_auto_scaling.types.launch_template_overrides.LaunchTemplateOverrides"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: Overrides, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.launch_template_overrides

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.launch_template_overrides.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Overrides:
    import capo_auto_scaling.types.launch_template_overrides

    out: Overrides = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.launch_template_overrides.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: Overrides, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.launch_template_overrides

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.launch_template_overrides.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Overrides:
    import capo_auto_scaling.types.launch_template_overrides

    out: Overrides = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.launch_template_overrides.deserialize_query(child)
        )
    return out
