"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceResourceDriftsSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_instance_resource_drifts_summary

StackInstanceResourceDriftsSummaries: TypeAlias = list[
    "capo_cloudformation.types.stack_instance_resource_drifts_summary.StackInstanceResourceDriftsSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceResourceDriftsSummaries,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_cloudformation.types.stack_instance_resource_drifts_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_instance_resource_drifts_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackInstanceResourceDriftsSummaries:
    import capo_cloudformation.types.stack_instance_resource_drifts_summary

    out: StackInstanceResourceDriftsSummaries = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.stack_instance_resource_drifts_summary.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: StackInstanceResourceDriftsSummaries,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_cloudformation.types.stack_instance_resource_drifts_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_instance_resource_drifts_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> StackInstanceResourceDriftsSummaries:
    import capo_cloudformation.types.stack_instance_resource_drifts_summary

    out: StackInstanceResourceDriftsSummaries = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.stack_instance_resource_drifts_summary.deserialize_query(
                child
            )
        )
    return out
