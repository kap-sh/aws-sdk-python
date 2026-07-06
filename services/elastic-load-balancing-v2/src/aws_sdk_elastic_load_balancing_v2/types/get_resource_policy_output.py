"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.policy


class GetResourcePolicyOutput(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_elastic_load_balancing_v2.types.policy.Policy"]
    """<p>The content of the resource policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetResourcePolicyOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy" in value:
        pairs.append((f"{prefix}.Policy", str(value["policy"])))


def deserialize_query(el: Element) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out
