"""Generated from Smithy shape ``com.amazonaws.cloudformation#LastOperations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.operation_entry

LastOperations: TypeAlias = list[
    "aws_sdk_cloudformation.types.operation_entry.OperationEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LastOperations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.operation_entry

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.operation_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LastOperations:
    import aws_sdk_cloudformation.types.operation_entry

    out: LastOperations = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.operation_entry.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: LastOperations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.operation_entry

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.operation_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LastOperations:
    import aws_sdk_cloudformation.types.operation_entry

    out: LastOperations = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.operation_entry.deserialize_query(child)
        )
    return out
