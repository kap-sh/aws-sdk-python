"""Generated from Smithy shape ``com.amazonaws.shield#ListAttacksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.max_results
    import aws_sdk_shield.types.resource_arn_filter_list
    import aws_sdk_shield.types.time_range
    import aws_sdk_shield.types.token


class ListAttacksRequest(TypedDict):
    resource_arns: NotRequired[
        "aws_sdk_shield.types.resource_arn_filter_list.ResourceArnFilterList"
    ]
    """<p>The ARNs (Amazon Resource Names) of the resources that were attacked. If you leave this blank, all applicable resources for this account will be included.</p>"""
    start_time: NotRequired["aws_sdk_shield.types.time_range.TimeRange"]
    """<p>The start of the time period for the attacks. This is a <code>timestamp</code> type. The request syntax listing for this call indicates a <code>number</code> type, but you can provide the time in any valid <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp\">timestamp format</a> setting. </p>"""
    end_time: NotRequired["aws_sdk_shield.types.time_range.TimeRange"]
    """<p>The end of the time period for the attacks. This is a <code>timestamp</code> type. The request syntax listing for this call indicates a <code>number</code> type, but you can provide the time in any valid <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp\">timestamp format</a> setting. </p>"""
    next_token: NotRequired["aws_sdk_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>"""
    max_results: NotRequired["aws_sdk_shield.types.max_results.MaxResults"]
    """<p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAttacksRequest) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import aws_sdk_shield.types.resource_arn_filter_list

        out["ResourceArns"] = (
            aws_sdk_shield.types.resource_arn_filter_list.serialize_aws_json_1_1(
                value["resource_arns"]
            )
        )
    if "start_time" in value:
        import aws_sdk_shield.types.time_range

        out["StartTime"] = aws_sdk_shield.types.time_range.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_shield.types.time_range

        out["EndTime"] = aws_sdk_shield.types.time_range.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAttacksRequest:
    out: ListAttacksRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArns" in data:
        import aws_sdk_shield.types.resource_arn_filter_list

        out["resource_arns"] = (
            aws_sdk_shield.types.resource_arn_filter_list.deserialize_aws_json_1_1(
                data["ResourceArns"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_shield.types.time_range

        out["start_time"] = aws_sdk_shield.types.time_range.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_shield.types.time_range

        out["end_time"] = aws_sdk_shield.types.time_range.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
