"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookResultSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.hook_result_summary

HookResultSummaries: TypeAlias = list[
    "capo_cloudformation.types.hook_result_summary.HookResultSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: HookResultSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.hook_result_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.hook_result_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> HookResultSummaries:
    import capo_cloudformation.types.hook_result_summary

    out: HookResultSummaries = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.hook_result_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: HookResultSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.hook_result_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.hook_result_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> HookResultSummaries:
    import capo_cloudformation.types.hook_result_summary

    out: HookResultSummaries = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.hook_result_summary.deserialize_query(child)
        )
    return out
