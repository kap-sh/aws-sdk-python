"""Generated from Smithy shape ``com.amazonaws.autoscaling#SuspendedProcesses``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.suspended_process

SuspendedProcesses: TypeAlias = list[
    "capo_auto_scaling.types.suspended_process.SuspendedProcess"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SuspendedProcesses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.suspended_process

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.suspended_process.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SuspendedProcesses:
    import capo_auto_scaling.types.suspended_process

    out: SuspendedProcesses = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.suspended_process.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SuspendedProcesses, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.suspended_process

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.suspended_process.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SuspendedProcesses:
    import capo_auto_scaling.types.suspended_process

    out: SuspendedProcesses = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.suspended_process.deserialize_query(child))
    return out
