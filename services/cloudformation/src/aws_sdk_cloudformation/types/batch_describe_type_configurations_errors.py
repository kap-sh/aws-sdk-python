"""Generated from Smithy shape ``com.amazonaws.cloudformation#BatchDescribeTypeConfigurationsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.batch_describe_type_configurations_error

BatchDescribeTypeConfigurationsErrors: TypeAlias = list[
    "aws_sdk_cloudformation.types.batch_describe_type_configurations_error.BatchDescribeTypeConfigurationsError"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDescribeTypeConfigurationsErrors,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_cloudformation.types.batch_describe_type_configurations_error

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.batch_describe_type_configurations_error.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BatchDescribeTypeConfigurationsErrors:
    import aws_sdk_cloudformation.types.batch_describe_type_configurations_error

    out: BatchDescribeTypeConfigurationsErrors = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.batch_describe_type_configurations_error.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: BatchDescribeTypeConfigurationsErrors,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_cloudformation.types.batch_describe_type_configurations_error

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.batch_describe_type_configurations_error.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> BatchDescribeTypeConfigurationsErrors:
    import aws_sdk_cloudformation.types.batch_describe_type_configurations_error

    out: BatchDescribeTypeConfigurationsErrors = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.batch_describe_type_configurations_error.deserialize_query(
                child
            )
        )
    return out
