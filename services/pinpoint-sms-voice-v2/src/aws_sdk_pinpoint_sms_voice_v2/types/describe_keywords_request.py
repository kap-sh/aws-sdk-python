"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeKeywordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_list
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn


class DescribeKeywordsRequest(TypedDict, closed=True):
    origination_identity: (
        "aws_sdk_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn"
    )
    """<p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    keywords: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.keyword_list.KeywordList"
    ]
    """<p>An array of keywords to search for.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_list.KeywordFilterList"
    ]
    """<p>An array of keyword filters to filter the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeKeywordsRequest) -> dict:
    out: dict = {}
    out["OriginationIdentity"] = value["origination_identity"]
    if "keywords" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.keyword_list

        out["Keywords"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_list.serialize_aws_json_1_0(
                value["keywords"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeKeywordsRequest:
    out: DescribeKeywordsRequest = {}  # type: ignore[typeddict-item]
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError(
            "DescribeKeywordsRequest.origination_identity required"
        )
    if "Keywords" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.keyword_list

        out["keywords"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_list.deserialize_aws_json_1_0(
                data["Keywords"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
