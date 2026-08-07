"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeTerminationPolicyTypesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.termination_policies


class DescribeTerminationPolicyTypesAnswer(TypedDict, closed=True):
    termination_policy_types: NotRequired[
        "capo_auto_scaling.types.termination_policies.TerminationPolicies"
    ]
    """<p>The termination policies supported by Amazon EC2 Auto Scaling: <code>OldestInstance</code>, <code>OldestLaunchConfiguration</code>, <code>NewestInstance</code>, <code>ClosestToNextInstanceHour</code>, <code>Default</code>, <code>OldestLaunchTemplate</code>, and <code>AllocationStrategy</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTerminationPolicyTypesAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "termination_policy_types" in value:
        import capo_auto_scaling.types.termination_policies

        capo_auto_scaling.types.termination_policies.serialize_query(
            value["termination_policy_types"],
            pairs,
            f"{key_prefix}TerminationPolicyTypes",
        )


def deserialize_query(el: Element) -> DescribeTerminationPolicyTypesAnswer:
    out: DescribeTerminationPolicyTypesAnswer = {}  # type: ignore[typeddict-item]
    child_termination_policy_types = el.find("TerminationPolicyTypes")
    if child_termination_policy_types is not None:
        import capo_auto_scaling.types.termination_policies

        out["termination_policy_types"] = (
            capo_auto_scaling.types.termination_policies.deserialize_query(
                child_termination_policy_types
            )
        )
    return out
