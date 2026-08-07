"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeletePolicyType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.xml_string_max_len255


class DeletePolicyType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    policy_name: NotRequired["capo_auto_scaling.types.resource_name.ResourceName"]
    """<p>The name or Amazon Resource Name (ARN) of the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePolicyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "policy_name" in value:
        pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))


def deserialize_query(el: Element) -> DeletePolicyType:
    out: DeletePolicyType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    return out
