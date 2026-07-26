"""Generated from Smithy shape ``com.amazonaws.autoscaling#StepAdjustments``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.step_adjustment

StepAdjustments: TypeAlias = list[
    "capo_auto_scaling.types.step_adjustment.StepAdjustment"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StepAdjustments, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.step_adjustment

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.step_adjustment.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StepAdjustments:
    import capo_auto_scaling.types.step_adjustment

    out: StepAdjustments = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.step_adjustment.deserialize_query(child))
    return out


def serialize_query_flat(
    value: StepAdjustments, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.step_adjustment

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.step_adjustment.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StepAdjustments:
    import capo_auto_scaling.types.step_adjustment

    out: StepAdjustments = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.step_adjustment.deserialize_query(child))
    return out
