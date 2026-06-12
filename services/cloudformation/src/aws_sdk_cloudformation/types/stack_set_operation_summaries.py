"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_set_operation_summary

StackSetOperationSummaries: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_set_operation_summary.StackSetOperationSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperationSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_set_operation_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_set_operation_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackSetOperationSummaries:
    import aws_sdk_cloudformation.types.stack_set_operation_summary

    out: StackSetOperationSummaries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_set_operation_summary.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: StackSetOperationSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_set_operation_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_set_operation_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackSetOperationSummaries:
    import aws_sdk_cloudformation.types.stack_set_operation_summary

    out: StackSetOperationSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_set_operation_summary.deserialize_query(
                child
            )
        )
    return out
