"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeSpendLimitsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.spend_limit_list


class DescribeSpendLimitsResult(TypedDict, closed=True):
    spend_limits: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.spend_limit_list.SpendLimitList"
    ]
    """<p>An array of SpendLimit objects that contain the details for the requested spend limits.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeSpendLimitsResult) -> dict:
    out: dict = {}
    if "spend_limits" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.spend_limit_list

        out["SpendLimits"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.spend_limit_list.serialize_aws_json_1_0(
                value["spend_limits"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeSpendLimitsResult:
    out: DescribeSpendLimitsResult = {}  # type: ignore[typeddict-item]
    if "SpendLimits" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.spend_limit_list

        out["spend_limits"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.spend_limit_list.deserialize_aws_json_1_0(
                data["SpendLimits"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
