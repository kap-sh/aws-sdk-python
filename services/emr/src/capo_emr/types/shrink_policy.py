"""Generated from Smithy shape ``com.amazonaws.emr#ShrinkPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_resize_policy
    import capo_emr.types.integer


class ShrinkPolicy(TypedDict, closed=True):
    decommission_timeout: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.</p>"""
    instance_resize_policy: NotRequired[
        "capo_emr.types.instance_resize_policy.InstanceResizePolicy"
    ]
    """<p>Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShrinkPolicy) -> dict:
    out: dict = {}
    if "decommission_timeout" in value:
        out["DecommissionTimeout"] = value["decommission_timeout"]
    if "instance_resize_policy" in value:
        import capo_emr.types.instance_resize_policy

        out["InstanceResizePolicy"] = (
            capo_emr.types.instance_resize_policy.serialize_aws_json_1_1(
                value["instance_resize_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShrinkPolicy:
    out: ShrinkPolicy = {}  # type: ignore[typeddict-item]
    if "DecommissionTimeout" in data:
        out["decommission_timeout"] = data["DecommissionTimeout"]
    if "InstanceResizePolicy" in data:
        import capo_emr.types.instance_resize_policy

        out["instance_resize_policy"] = (
            capo_emr.types.instance_resize_policy.deserialize_aws_json_1_1(
                data["InstanceResizePolicy"]
            )
        )
    return out
