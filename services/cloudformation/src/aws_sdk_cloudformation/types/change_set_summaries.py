"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_summary

ChangeSetSummaries: TypeAlias = list[
    "aws_sdk_cloudformation.types.change_set_summary.ChangeSetSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.change_set_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.change_set_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ChangeSetSummaries:
    import aws_sdk_cloudformation.types.change_set_summary

    out: ChangeSetSummaries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.change_set_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ChangeSetSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.change_set_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.change_set_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ChangeSetSummaries:
    import aws_sdk_cloudformation.types.change_set_summary

    out: ChangeSetSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.change_set_summary.deserialize_query(child)
        )
    return out
