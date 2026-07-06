"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateUsageLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.usage_limit_breach_action
    import aws_sdk_redshift_serverless.types.usage_limit_period
    import aws_sdk_redshift_serverless.types.usage_limit_usage_type


class CreateUsageLimitRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.</p>"""
    usage_type: (
        "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
    )
    """<p>The type of Amazon Redshift Serverless usage to create a usage limit for.</p>"""
    amount: "int"
    """<p>The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>"""
    period: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_period.UsageLimitPeriod"
    ]
    """<p>The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.</p>"""
    breach_action: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUsageLimitRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["usageType"] = value["usage_type"]
    out["amount"] = value["amount"]
    if "period" in value:
        out["period"] = value["period"]
    if "breach_action" in value:
        out["breachAction"] = value["breach_action"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUsageLimitRequest:
    out: CreateUsageLimitRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("CreateUsageLimitRequest.resource_arn required")
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    else:
        raise DeserializationError("CreateUsageLimitRequest.usage_type required")
    if "amount" in data:
        out["amount"] = data["amount"]
    else:
        raise DeserializationError("CreateUsageLimitRequest.amount required")
    if "period" in data:
        out["period"] = data["period"]
    if "breachAction" in data:
        out["breach_action"] = data["breachAction"]
    return out
