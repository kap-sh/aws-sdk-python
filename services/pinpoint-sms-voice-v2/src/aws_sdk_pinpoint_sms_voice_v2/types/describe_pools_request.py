"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribePoolsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.owner
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_id_list


class DescribePoolsRequest(TypedDict):
    pool_ids: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.pool_id_list.PoolIdList"]
    """<p>The unique identifier of pools to find. This is an array of strings that can be either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.pool_filter_list.PoolFilterList"
    ]
    """<p>An array of PoolFilter objects to filter the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""
    owner: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.owner.Owner"]
    """<p>Use <code>SELF</code> to filter the list of Pools to ones your account owns or use <code>SHARED</code> to filter on Pools shared with your account. The <code>Owner</code> and <code>PoolIds</code> parameters can't be used at the same time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribePoolsRequest) -> dict:
    out: dict = {}
    if "pool_ids" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.pool_id_list

        out["PoolIds"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.pool_id_list.serialize_aws_json_1_0(
                value["pool_ids"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.pool_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.pool_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribePoolsRequest:
    out: DescribePoolsRequest = {}  # type: ignore[typeddict-item]
    if "PoolIds" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.pool_id_list

        out["pool_ids"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.pool_id_list.deserialize_aws_json_1_0(
                data["PoolIds"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.pool_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.pool_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
