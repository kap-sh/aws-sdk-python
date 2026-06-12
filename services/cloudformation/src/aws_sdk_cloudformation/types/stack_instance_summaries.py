"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_instance_summary

StackInstanceSummaries: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_instance_summary.StackInstanceSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_instance_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_instance_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackInstanceSummaries:
    import aws_sdk_cloudformation.types.stack_instance_summary

    out: StackInstanceSummaries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_instance_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackInstanceSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_instance_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_instance_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackInstanceSummaries:
    import aws_sdk_cloudformation.types.stack_instance_summary

    out: StackInstanceSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_instance_summary.deserialize_query(child)
        )
    return out
