"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.type_summary

TypeSummaries: TypeAlias = list["capo_cloudformation.types.type_summary.TypeSummary"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.type_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.type_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TypeSummaries:
    import capo_cloudformation.types.type_summary

    out: TypeSummaries = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.type_summary.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TypeSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.type_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.type_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TypeSummaries:
    import capo_cloudformation.types.type_summary

    out: TypeSummaries = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.type_summary.deserialize_query(child))
    return out
