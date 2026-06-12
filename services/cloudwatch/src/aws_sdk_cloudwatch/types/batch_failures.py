"""Generated from Smithy shape ``com.amazonaws.cloudwatch#BatchFailures``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.partial_failure

BatchFailures: TypeAlias = list[
    "aws_sdk_cloudwatch.types.partial_failure.PartialFailure"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchFailures, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.partial_failure

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.partial_failure.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BatchFailures:
    import aws_sdk_cloudwatch.types.partial_failure

    out: BatchFailures = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudwatch.types.partial_failure.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BatchFailures, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.partial_failure

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.partial_failure.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BatchFailures:
    import aws_sdk_cloudwatch.types.partial_failure

    out: BatchFailures = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudwatch.types.partial_failure.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchFailures) -> list:
    import aws_sdk_cloudwatch.types.partial_failure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.partial_failure.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchFailures:
    import aws_sdk_cloudwatch.types.partial_failure

    out: BatchFailures = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.partial_failure.deserialize_aws_json_1_0(item)
        )
    return out
