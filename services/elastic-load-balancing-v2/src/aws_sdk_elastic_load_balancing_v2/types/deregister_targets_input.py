"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DeregisterTargetsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_descriptions
    import aws_sdk_elastic_load_balancing_v2.types.target_group_arn


class DeregisterTargetsInput(TypedDict):
    target_group_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_group_arn.TargetGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    targets: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_descriptions.TargetDescriptions"
    ]
    """<p>The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterTargetsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_group_arn" in value:
        pairs.append((f"{prefix}.TargetGroupArn", str(value["target_group_arn"])))
    if "targets" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_descriptions

        aws_sdk_elastic_load_balancing_v2.types.target_descriptions.serialize_query(
            value["targets"], pairs, f"{prefix}.Targets"
        )


def deserialize_query(el: Element) -> DeregisterTargetsInput:
    out: DeregisterTargetsInput = {}  # type: ignore[typeddict-item]
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_targets = el.find("Targets")
    if child_targets is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_descriptions

        out["targets"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_descriptions.deserialize_query(
                child_targets
            )
        )
    return out
