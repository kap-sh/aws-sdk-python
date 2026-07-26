"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorExecutionStatusFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_refactor_execution_status

StackRefactorExecutionStatusFilter: TypeAlias = list[
    "capo_cloudformation.types.stack_refactor_execution_status.StackRefactorExecutionStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackRefactorExecutionStatusFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.stack_refactor_execution_status

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_refactor_execution_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackRefactorExecutionStatusFilter:
    import capo_cloudformation.types.stack_refactor_execution_status

    out: StackRefactorExecutionStatusFilter = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.stack_refactor_execution_status.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: StackRefactorExecutionStatusFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.stack_refactor_execution_status

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_refactor_execution_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> StackRefactorExecutionStatusFilter:
    import capo_cloudformation.types.stack_refactor_execution_status

    out: StackRefactorExecutionStatusFilter = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.stack_refactor_execution_status.deserialize_query(
                child
            )
        )
    return out
