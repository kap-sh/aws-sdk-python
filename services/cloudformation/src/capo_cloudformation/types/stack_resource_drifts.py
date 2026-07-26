"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDrifts``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_resource_drift

StackResourceDrifts: TypeAlias = list[
    "capo_cloudformation.types.stack_resource_drift.StackResourceDrift"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceDrifts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.stack_resource_drift

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_resource_drift.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackResourceDrifts:
    import capo_cloudformation.types.stack_resource_drift

    out: StackResourceDrifts = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.stack_resource_drift.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackResourceDrifts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.stack_resource_drift

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_resource_drift.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackResourceDrifts:
    import capo_cloudformation.types.stack_resource_drift

    out: StackResourceDrifts = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.stack_resource_drift.deserialize_query(child)
        )
    return out
