"""Generated from Smithy shape ``com.amazonaws.emr#ScalingAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.market_type
    import aws_sdk_emr.types.simple_scaling_policy_configuration


class ScalingAction(TypedDict, closed=True):
    market: NotRequired["aws_sdk_emr.types.market_type.MarketType"]
    """<p>Not available for instance groups. Instance groups use the market type specified for the group.</p>"""
    simple_scaling_policy_configuration: NotRequired[
        "aws_sdk_emr.types.simple_scaling_policy_configuration.SimpleScalingPolicyConfiguration"
    ]
    """<p>The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingAction) -> dict:
    out: dict = {}
    if "market" in value:
        import aws_sdk_emr.types.market_type

        out["Market"] = aws_sdk_emr.types.market_type.serialize_aws_json_1_1(
            value["market"]
        )
    if "simple_scaling_policy_configuration" in value:
        import aws_sdk_emr.types.simple_scaling_policy_configuration

        out["SimpleScalingPolicyConfiguration"] = (
            aws_sdk_emr.types.simple_scaling_policy_configuration.serialize_aws_json_1_1(
                value["simple_scaling_policy_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingAction:
    out: ScalingAction = {}  # type: ignore[typeddict-item]
    if "Market" in data:
        import aws_sdk_emr.types.market_type

        out["market"] = aws_sdk_emr.types.market_type.deserialize_aws_json_1_1(
            data["Market"]
        )
    if "SimpleScalingPolicyConfiguration" in data:
        import aws_sdk_emr.types.simple_scaling_policy_configuration

        out["simple_scaling_policy_configuration"] = (
            aws_sdk_emr.types.simple_scaling_policy_configuration.deserialize_aws_json_1_1(
                data["SimpleScalingPolicyConfiguration"]
            )
        )
    return out
