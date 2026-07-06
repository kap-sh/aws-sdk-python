"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroupTuple``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn
    import aws_sdk_elastic_load_balancing_v2.types.target_group_weight


class TargetGroupTuple(TypedDict, closed=True):
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    weight: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_weight.TargetGroupWeight"
    ]
    """<p>The weight. The range is 0 to 999.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroupTuple, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "weight" in value:
        pairs.append((f"{prefix}.Weight", str(value["weight"])))


def deserialize_query(el: Element) -> TargetGroupTuple:
    out: TargetGroupTuple = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_weight = el.find("Weight")
    if child_weight is not None:
        out["weight"] = int(child_weight.text or "")
    return out
