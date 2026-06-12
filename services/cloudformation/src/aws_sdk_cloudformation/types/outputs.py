"""Generated from Smithy shape ``com.amazonaws.cloudformation#Outputs``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.output

Outputs: TypeAlias = list["aws_sdk_cloudformation.types.output.Output"]


# --- awsQuery ser/de ---
def serialize_query(value: Outputs, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_cloudformation.types.output

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.output.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Outputs:
    import aws_sdk_cloudformation.types.output

    out: Outputs = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.output.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Outputs, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.output

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.output.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Outputs:
    import aws_sdk_cloudformation.types.output

    out: Outputs = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.output.deserialize_query(child))
    return out
