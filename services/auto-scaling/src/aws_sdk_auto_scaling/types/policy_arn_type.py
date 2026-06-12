"""Generated from Smithy shape ``com.amazonaws.autoscaling#PolicyARNType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.alarms
    import aws_sdk_auto_scaling.types.resource_name


class PolicyARNType(TypedDict):
    policy_arn: NotRequired["aws_sdk_auto_scaling.types.resource_name.ResourceName"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    alarms: NotRequired["aws_sdk_auto_scaling.types.alarms.Alarms"]
    """<p>The CloudWatch alarms created for the target tracking scaling policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyARNType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_arn" in value:
        pairs.append((f"{prefix}.PolicyARN", str(value["policy_arn"])))
    if "alarms" in value:
        import aws_sdk_auto_scaling.types.alarms

        aws_sdk_auto_scaling.types.alarms.serialize_query(
            value["alarms"], pairs, f"{prefix}.Alarms"
        )


def deserialize_query(el: Element) -> PolicyARNType:
    out: PolicyARNType = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyARN")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    child_alarms = el.find("Alarms")
    if child_alarms is not None:
        import aws_sdk_auto_scaling.types.alarms

        out["alarms"] = aws_sdk_auto_scaling.types.alarms.deserialize_query(
            child_alarms
        )
    return out
