"""Generated from Smithy shape ``com.amazonaws.autoscaling#Processes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.process_type

Processes: TypeAlias = list["capo_auto_scaling.types.process_type.ProcessType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Processes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.process_type

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.process_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Processes:
    import capo_auto_scaling.types.process_type

    out: Processes = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.process_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Processes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.process_type

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.process_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Processes:
    import capo_auto_scaling.types.process_type

    out: Processes = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.process_type.deserialize_query(child))
    return out
