"""Generated from Smithy shape ``com.amazonaws.cloudformation#Exports``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.export

Exports: TypeAlias = list["capo_cloudformation.types.export.Export"]


# --- awsQuery ser/de ---
def serialize_query(value: Exports, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_cloudformation.types.export

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.export.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Exports:
    import capo_cloudformation.types.export

    out: Exports = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.export.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Exports, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.export

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.export.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Exports:
    import capo_cloudformation.types.export

    out: Exports = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.export.deserialize_query(child))
    return out
