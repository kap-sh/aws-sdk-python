"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeKeywordsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_information_list
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token


class DescribeKeywordsResult(TypedDict):
    origination_identity_arn: NotRequired["str"]
    """<p>The PhoneNumberArn or PoolArn that is associated with the OriginationIdentity. </p>"""
    origination_identity: NotRequired["str"]
    """<p>The PhoneNumberId or PoolId that is associated with the OriginationIdentity.</p>"""
    keywords: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.keyword_information_list.KeywordInformationList"
    ]
    """<p>An array of KeywordInformation objects that contain the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeKeywordsResult) -> dict:
    out: dict = {}
    if "origination_identity_arn" in value:
        out["OriginationIdentityArn"] = value["origination_identity_arn"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "keywords" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.keyword_information_list

        out["Keywords"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_information_list.serialize_aws_json_1_0(
                value["keywords"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeKeywordsResult:
    out: DescribeKeywordsResult = {}  # type: ignore[typeddict-item]
    if "OriginationIdentityArn" in data:
        out["origination_identity_arn"] = data["OriginationIdentityArn"]
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    if "Keywords" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.keyword_information_list

        out["keywords"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_information_list.deserialize_aws_json_1_0(
                data["Keywords"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
