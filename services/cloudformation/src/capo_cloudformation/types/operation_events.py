"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.operation_event

OperationEvents: TypeAlias = list[
    "capo_cloudformation.types.operation_event.OperationEvent"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationEvents, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.operation_event

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.operation_event.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> OperationEvents:
    import capo_cloudformation.types.operation_event

    out: OperationEvents = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.operation_event.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OperationEvents, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.operation_event

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.operation_event.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OperationEvents:
    import capo_cloudformation.types.operation_event

    out: OperationEvents = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.operation_event.deserialize_query(child))
    return out
