"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDriftStatusFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_resource_drift_status

StackResourceDriftStatusFilters: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_resource_drift_status.StackResourceDriftStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceDriftStatusFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_resource_drift_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_resource_drift_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackResourceDriftStatusFilters:
    import aws_sdk_cloudformation.types.stack_resource_drift_status

    out: StackResourceDriftStatusFilters = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: StackResourceDriftStatusFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_resource_drift_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_resource_drift_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> StackResourceDriftStatusFilters:
    import aws_sdk_cloudformation.types.stack_resource_drift_status

    out: StackResourceDriftStatusFilters = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child
            )
        )
    return out
