"""Generated from Smithy shape ``com.amazonaws.cloudformation#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.parameter

Parameters: TypeAlias = list["aws_sdk_cloudformation.types.parameter.Parameter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Parameters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.parameter

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.parameter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Parameters:
    import aws_sdk_cloudformation.types.parameter

    out: Parameters = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.parameter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Parameters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.parameter

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.parameter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Parameters:
    import aws_sdk_cloudformation.types.parameter

    out: Parameters = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.parameter.deserialize_query(child))
    return out
