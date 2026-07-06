"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UsageLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.usage_limit_breach_action
    import aws_sdk_redshift_serverless.types.usage_limit_period
    import aws_sdk_redshift_serverless.types.usage_limit_usage_type


class UsageLimit(TypedDict, closed=True):
    usage_limit_id: NotRequired["str"]
    """<p>The identifier of the usage limit.</p>"""
    usage_limit_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the resource associated with the usage limit.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) that identifies the Amazon Redshift Serverless resource.</p>"""
    usage_type: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
    ]
    """<p>The Amazon Redshift Serverless feature to limit.</p>"""
    amount: NotRequired["int"]
    """<p>The limit amount. If time-based, this amount is in RPUs consumed per hour. If data-based, this amount is in terabytes (TB). The value must be a positive number.</p>"""
    period: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_period.UsageLimitPeriod"
    ]
    """<p>The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.</p>"""
    breach_action: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The action that Amazon Redshift Serverless takes when the limit is reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageLimit) -> dict:
    out: dict = {}
    if "usage_limit_id" in value:
        out["usageLimitId"] = value["usage_limit_id"]
    if "usage_limit_arn" in value:
        out["usageLimitArn"] = value["usage_limit_arn"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "amount" in value:
        out["amount"] = value["amount"]
    if "period" in value:
        out["period"] = value["period"]
    if "breach_action" in value:
        out["breachAction"] = value["breach_action"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageLimit:
    out: UsageLimit = {}  # type: ignore[typeddict-item]
    if "usageLimitId" in data:
        out["usage_limit_id"] = data["usageLimitId"]
    if "usageLimitArn" in data:
        out["usage_limit_arn"] = data["usageLimitArn"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    if "amount" in data:
        out["amount"] = data["amount"]
    if "period" in data:
        out["period"] = data["period"]
    if "breachAction" in data:
        out["breach_action"] = data["breachAction"]
    return out
