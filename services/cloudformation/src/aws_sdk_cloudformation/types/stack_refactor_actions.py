"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorActions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_refactor_action

StackRefactorActions: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_refactor_action.StackRefactorAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackRefactorActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_refactor_action

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_refactor_action.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackRefactorActions:
    import aws_sdk_cloudformation.types.stack_refactor_action

    out: StackRefactorActions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_refactor_action.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackRefactorActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_refactor_action

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_refactor_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackRefactorActions:
    import aws_sdk_cloudformation.types.stack_refactor_action

    out: StackRefactorActions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_refactor_action.deserialize_query(child)
        )
    return out
