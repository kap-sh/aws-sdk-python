"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorUntagResources``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.tag_key

StackRefactorUntagResources: TypeAlias = list[
    "aws_sdk_cloudformation.types.tag_key.TagKey"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackRefactorUntagResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> StackRefactorUntagResources:
    out: StackRefactorUntagResources = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: StackRefactorUntagResources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> StackRefactorUntagResources:
    out: StackRefactorUntagResources = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
