"""Generated from Smithy shape ``com.amazonaws.sts#ProvidedContextsListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.provided_context

ProvidedContextsListType: TypeAlias = list[
    "capo_sts.types.provided_context.ProvidedContext"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ProvidedContextsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sts.types.provided_context

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sts.types.provided_context.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ProvidedContextsListType:
    import capo_sts.types.provided_context

    out: ProvidedContextsListType = []
    for child in el.findall("member"):
        out.append(capo_sts.types.provided_context.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ProvidedContextsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sts.types.provided_context

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sts.types.provided_context.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ProvidedContextsListType:
    import capo_sts.types.provided_context

    out: ProvidedContextsListType = []
    for child in parent.findall(tag):
        out.append(capo_sts.types.provided_context.deserialize_query(child))
    return out
