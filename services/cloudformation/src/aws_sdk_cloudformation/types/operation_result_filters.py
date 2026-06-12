"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationResultFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.operation_result_filter

OperationResultFilters: TypeAlias = list[
    "aws_sdk_cloudformation.types.operation_result_filter.OperationResultFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationResultFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.operation_result_filter

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.operation_result_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> OperationResultFilters:
    import aws_sdk_cloudformation.types.operation_result_filter

    out: OperationResultFilters = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.operation_result_filter.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: OperationResultFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.operation_result_filter

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.operation_result_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OperationResultFilters:
    import aws_sdk_cloudformation.types.operation_result_filter

    out: OperationResultFilters = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.operation_result_filter.deserialize_query(
                child
            )
        )
    return out
