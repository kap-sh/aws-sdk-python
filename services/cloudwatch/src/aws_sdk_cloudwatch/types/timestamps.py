"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Timestamps``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.timestamp

Timestamps: TypeAlias = list["aws_sdk_cloudwatch.types.timestamp.Timestamp"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Timestamps, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.timestamp

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Timestamps:
    import aws_sdk_cloudwatch.types.timestamp

    out: Timestamps = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudwatch.types.timestamp.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Timestamps, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.timestamp

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.timestamp.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Timestamps:
    import aws_sdk_cloudwatch.types.timestamp

    out: Timestamps = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudwatch.types.timestamp.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Timestamps) -> list:
    import aws_sdk_cloudwatch.types.timestamp

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Timestamps:
    import aws_sdk_cloudwatch.types.timestamp

    out: Timestamps = []
    for item in data:
        out.append(aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(item))
    return out
