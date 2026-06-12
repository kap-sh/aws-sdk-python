"""Generated from Smithy shape ``com.amazonaws.cloudformation#Scope``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_attribute

Scope: TypeAlias = list[
    "aws_sdk_cloudformation.types.resource_attribute.ResourceAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(value: Scope, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_cloudformation.types.resource_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Scope:
    import aws_sdk_cloudformation.types.resource_attribute

    out: Scope = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.resource_attribute.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: Scope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Scope:
    import aws_sdk_cloudformation.types.resource_attribute

    out: Scope = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.resource_attribute.deserialize_query(child)
        )
    return out
