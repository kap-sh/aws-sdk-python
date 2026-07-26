"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetAutoDeploymentTargetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_set_auto_deployment_target_summary

StackSetAutoDeploymentTargetSummaries: TypeAlias = list[
    "capo_cloudformation.types.stack_set_auto_deployment_target_summary.StackSetAutoDeploymentTargetSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetAutoDeploymentTargetSummaries,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_cloudformation.types.stack_set_auto_deployment_target_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_set_auto_deployment_target_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> StackSetAutoDeploymentTargetSummaries:
    import capo_cloudformation.types.stack_set_auto_deployment_target_summary

    out: StackSetAutoDeploymentTargetSummaries = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.stack_set_auto_deployment_target_summary.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: StackSetAutoDeploymentTargetSummaries,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_cloudformation.types.stack_set_auto_deployment_target_summary

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.stack_set_auto_deployment_target_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> StackSetAutoDeploymentTargetSummaries:
    import capo_cloudformation.types.stack_set_auto_deployment_target_summary

    out: StackSetAutoDeploymentTargetSummaries = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.stack_set_auto_deployment_target_summary.deserialize_query(
                child
            )
        )
    return out
