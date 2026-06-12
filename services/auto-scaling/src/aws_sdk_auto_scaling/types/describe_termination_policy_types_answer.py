"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeTerminationPolicyTypesAnswer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.termination_policies


class DescribeTerminationPolicyTypesAnswer(TypedDict):
    termination_policy_types: NotRequired[
        "aws_sdk_auto_scaling.types.termination_policies.TerminationPolicies"
    ]
    """<p>The termination policies supported by Amazon EC2 Auto Scaling: <code>OldestInstance</code>, <code>OldestLaunchConfiguration</code>, <code>NewestInstance</code>, <code>ClosestToNextInstanceHour</code>, <code>Default</code>, <code>OldestLaunchTemplate</code>, and <code>AllocationStrategy</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTerminationPolicyTypesAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "termination_policy_types" in value:
        import aws_sdk_auto_scaling.types.termination_policies

        aws_sdk_auto_scaling.types.termination_policies.serialize_query(
            value["termination_policy_types"], pairs, f"{prefix}.TerminationPolicyTypes"
        )


def deserialize_query(el: Element) -> DescribeTerminationPolicyTypesAnswer:
    out: DescribeTerminationPolicyTypesAnswer = {}  # type: ignore[typeddict-item]
    child_termination_policy_types = el.find("TerminationPolicyTypes")
    if child_termination_policy_types is not None:
        import aws_sdk_auto_scaling.types.termination_policies

        out["termination_policy_types"] = (
            aws_sdk_auto_scaling.types.termination_policies.deserialize_query(
                child_termination_policy_types
            )
        )
    return out
