"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_set_summary

StackSetSummaries: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_set_summary.StackSetSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_set_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_set_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackSetSummaries:
    import aws_sdk_cloudformation.types.stack_set_summary

    out: StackSetSummaries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_set_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackSetSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_set_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_set_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackSetSummaries:
    import aws_sdk_cloudformation.types.stack_set_summary

    out: StackSetSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_set_summary.deserialize_query(child)
        )
    return out
