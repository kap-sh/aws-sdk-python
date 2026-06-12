"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorTagResources``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.tag

StackRefactorTagResources: TypeAlias = list["aws_sdk_cloudformation.types.tag.Tag"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackRefactorTagResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.tag

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.tag.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackRefactorTagResources:
    import aws_sdk_cloudformation.types.tag

    out: StackRefactorTagResources = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: StackRefactorTagResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.tag

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> StackRefactorTagResources:
    import aws_sdk_cloudformation.types.tag

    out: StackRefactorTagResources = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.tag.deserialize_query(child))
    return out
