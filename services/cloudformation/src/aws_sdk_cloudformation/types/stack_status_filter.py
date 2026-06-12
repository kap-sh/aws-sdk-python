"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackStatusFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_status

StackStatusFilter: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_status.StackStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackStatusFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackStatusFilter:
    import aws_sdk_cloudformation.types.stack_status

    out: StackStatusFilter = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.stack_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: StackStatusFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackStatusFilter:
    import aws_sdk_cloudformation.types.stack_status

    out: StackStatusFilter = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.stack_status.deserialize_query(child))
    return out
