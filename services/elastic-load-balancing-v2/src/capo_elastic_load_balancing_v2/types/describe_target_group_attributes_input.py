"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetGroupAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.target_group_arn


class DescribeTargetGroupAttributesInput(TypedDict, closed=True):
    target_group_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTargetGroupAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_group_arn" in value:
        pairs.append((f"{key_prefix}TargetGroupArn", str(value["target_group_arn"])))


def deserialize_query(el: Element) -> DescribeTargetGroupAttributesInput:
    out: DescribeTargetGroupAttributesInput = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    return out
