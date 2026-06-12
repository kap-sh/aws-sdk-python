"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_definition

StackDefinitions: TypeAlias = list[
    "aws_sdk_cloudformation.types.stack_definition.StackDefinition"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackDefinitions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_definition

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_definition.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackDefinitions:
    import aws_sdk_cloudformation.types.stack_definition

    out: StackDefinitions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.stack_definition.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: StackDefinitions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.stack_definition

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.stack_definition.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> StackDefinitions:
    import aws_sdk_cloudformation.types.stack_definition

    out: StackDefinitions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.stack_definition.deserialize_query(child)
        )
    return out
