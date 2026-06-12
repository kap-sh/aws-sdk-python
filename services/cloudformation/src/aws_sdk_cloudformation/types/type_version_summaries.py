"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.type_version_summary

TypeVersionSummaries: TypeAlias = list[
    "aws_sdk_cloudformation.types.type_version_summary.TypeVersionSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeVersionSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.type_version_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.type_version_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TypeVersionSummaries:
    import aws_sdk_cloudformation.types.type_version_summary

    out: TypeVersionSummaries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.type_version_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TypeVersionSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.type_version_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.type_version_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TypeVersionSummaries:
    import aws_sdk_cloudformation.types.type_version_summary

    out: TypeVersionSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.type_version_summary.deserialize_query(child)
        )
    return out
