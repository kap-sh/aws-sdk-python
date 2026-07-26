"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.type_version_summary

TypeVersionSummaries: TypeAlias = list[
    "capo_cloudformation.types.type_version_summary.TypeVersionSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeVersionSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.type_version_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.type_version_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TypeVersionSummaries:
    import capo_cloudformation.types.type_version_summary

    out: TypeVersionSummaries = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.type_version_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TypeVersionSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.type_version_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.type_version_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TypeVersionSummaries:
    import capo_cloudformation.types.type_version_summary

    out: TypeVersionSummaries = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.type_version_summary.deserialize_query(child)
        )
    return out
