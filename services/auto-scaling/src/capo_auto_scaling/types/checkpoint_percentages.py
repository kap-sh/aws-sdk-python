"""Generated from Smithy shape ``com.amazonaws.autoscaling#CheckpointPercentages``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.non_zero_int_percent

CheckpointPercentages: TypeAlias = list[
    "capo_auto_scaling.types.non_zero_int_percent.NonZeroIntPercent"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CheckpointPercentages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> CheckpointPercentages:
    out: CheckpointPercentages = []
    for child in el.findall("member"):
        out.append(int(child.text or ""))
    return out


def serialize_query_flat(
    value: CheckpointPercentages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> CheckpointPercentages:
    out: CheckpointPercentages = []
    for child in parent.findall(tag):
        out.append(int(child.text or ""))
    return out
