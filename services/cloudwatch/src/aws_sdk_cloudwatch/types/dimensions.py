"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dimension

Dimensions: TypeAlias = list["aws_sdk_cloudwatch.types.dimension.Dimension"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Dimensions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.dimension

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.dimension.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Dimensions:
    import aws_sdk_cloudwatch.types.dimension

    out: Dimensions = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudwatch.types.dimension.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Dimensions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.dimension

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.dimension.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Dimensions:
    import aws_sdk_cloudwatch.types.dimension

    out: Dimensions = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudwatch.types.dimension.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimensions) -> list:
    import aws_sdk_cloudwatch.types.dimension

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch.types.dimension.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Dimensions:
    import aws_sdk_cloudwatch.types.dimension

    out: Dimensions = []
    for item in data:
        out.append(aws_sdk_cloudwatch.types.dimension.deserialize_aws_json_1_0(item))
    return out
