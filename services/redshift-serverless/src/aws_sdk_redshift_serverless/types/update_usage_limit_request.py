"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateUsageLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.usage_limit_breach_action


class UpdateUsageLimitRequest(TypedDict, closed=True):
    usage_limit_id: "str"
    """<p>The identifier of the usage limit to update.</p>"""
    amount: NotRequired["int"]
    """<p>The new limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>"""
    breach_action: NotRequired[
        "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The new action that Amazon Redshift Serverless takes when the limit is reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUsageLimitRequest) -> dict:
    out: dict = {}
    out["usageLimitId"] = value["usage_limit_id"]
    if "amount" in value:
        out["amount"] = value["amount"]
    if "breach_action" in value:
        out["breachAction"] = value["breach_action"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUsageLimitRequest:
    out: UpdateUsageLimitRequest = {}  # type: ignore[typeddict-item]
    if "usageLimitId" in data:
        out["usage_limit_id"] = data["usageLimitId"]
    else:
        raise DeserializationError("UpdateUsageLimitRequest.usage_limit_id required")
    if "amount" in data:
        out["amount"] = data["amount"]
    if "breachAction" in data:
        out["breach_action"] = data["breachAction"]
    return out
