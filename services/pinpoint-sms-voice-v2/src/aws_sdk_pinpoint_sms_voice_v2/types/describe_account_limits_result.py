"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeAccountLimitsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_limit_list
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token


class DescribeAccountLimitsResult(TypedDict, closed=True):
    account_limits: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.account_limit_list.AccountLimitList"
    ]
    """<p>An array of AccountLimit objects that show the current spend limits.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAccountLimitsResult) -> dict:
    out: dict = {}
    if "account_limits" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.account_limit_list

        out["AccountLimits"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.account_limit_list.serialize_aws_json_1_0(
                value["account_limits"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAccountLimitsResult:
    out: DescribeAccountLimitsResult = {}  # type: ignore[typeddict-item]
    if "AccountLimits" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.account_limit_list

        out["account_limits"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.account_limit_list.deserialize_aws_json_1_0(
                data["AccountLimits"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
