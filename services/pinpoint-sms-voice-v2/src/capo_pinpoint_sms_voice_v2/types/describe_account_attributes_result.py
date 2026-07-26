"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeAccountAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.account_attribute_list
    import capo_pinpoint_sms_voice_v2.types.next_token


class DescribeAccountAttributesResult(TypedDict, closed=True):
    account_attributes: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.account_attribute_list.AccountAttributeList"
    ]
    """<p>An array of AccountAttributes objects.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAccountAttributesResult) -> dict:
    out: dict = {}
    if "account_attributes" in value:
        import capo_pinpoint_sms_voice_v2.types.account_attribute_list

        out["AccountAttributes"] = (
            capo_pinpoint_sms_voice_v2.types.account_attribute_list.serialize_aws_json_1_0(
                value["account_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAccountAttributesResult:
    out: DescribeAccountAttributesResult = {}  # type: ignore[typeddict-item]
    if "AccountAttributes" in data:
        import capo_pinpoint_sms_voice_v2.types.account_attribute_list

        out["account_attributes"] = (
            capo_pinpoint_sms_voice_v2.types.account_attribute_list.deserialize_aws_json_1_0(
                data["AccountAttributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
