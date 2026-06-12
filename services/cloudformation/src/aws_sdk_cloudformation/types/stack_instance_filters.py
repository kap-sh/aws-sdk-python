"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_instance_filter

StackInstanceFilters: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_instance_filter.StackInstanceFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_instance_filter

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_instance_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackInstanceFilters:
    import aws_sdk_cloudformation.types.stack_instance_filter

    out: StackInstanceFilters = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_instance_filter.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackInstanceFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_instance_filter

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_instance_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackInstanceFilters:
    import aws_sdk_cloudformation.types.stack_instance_filter

    out: StackInstanceFilters = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_instance_filter.deserialize_query(child)
        )
    return out
