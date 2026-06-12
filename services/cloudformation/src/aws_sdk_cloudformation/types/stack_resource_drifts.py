"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDrifts``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_resource_drift

StackResourceDrifts: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_resource_drift.StackResourceDrift"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceDrifts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_resource_drift

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_resource_drift.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackResourceDrifts:
    import aws_sdk_cloudformation.types.stack_resource_drift

    out: StackResourceDrifts = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_resource_drift.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackResourceDrifts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_resource_drift

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_resource_drift.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackResourceDrifts:
    import aws_sdk_cloudformation.types.stack_resource_drift

    out: StackResourceDrifts = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_resource_drift.deserialize_query(child)
        )
    return out
