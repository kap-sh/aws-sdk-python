"""Generated from Smithy shape ``com.amazonaws.sts#ProvidedContextsListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.provided_context

ProvidedContextsListType: TypeAlias = list[
    "aws_sdk_sts.types.provided_context.ProvidedContext"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ProvidedContextsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sts.types.provided_context

    for n, item in enumerate(value, 1):
        aws_sdk_sts.types.provided_context.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ProvidedContextsListType:
    import aws_sdk_sts.types.provided_context

    out: ProvidedContextsListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_sts.types.provided_context.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ProvidedContextsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sts.types.provided_context

    for n, item in enumerate(value, 1):
        aws_sdk_sts.types.provided_context.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ProvidedContextsListType:
    import aws_sdk_sts.types.provided_context

    out: ProvidedContextsListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sts.types.provided_context.deserialize_query(child))
    return out
