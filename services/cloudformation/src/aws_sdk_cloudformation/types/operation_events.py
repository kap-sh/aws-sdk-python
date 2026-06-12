"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.operation_event

OperationEvents: TypeAlias = list[
    "aws_sdk_cloudformation.types.operation_event.OperationEvent"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationEvents, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.operation_event

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.operation_event.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> OperationEvents:
    import aws_sdk_cloudformation.types.operation_event

    out: OperationEvents = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.operation_event.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: OperationEvents, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.operation_event

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.operation_event.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OperationEvents:
    import aws_sdk_cloudformation.types.operation_event

    out: OperationEvents = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.operation_event.deserialize_query(child)
        )
    return out
