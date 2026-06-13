"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribePoolsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_information_list


class DescribePoolsResult(TypedDict):
    pools: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.pool_information_list.PoolInformationList"
    ]
    """<p>An array of PoolInformation objects that contain the details for the requested pools. </p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribePoolsResult) -> dict:
    out: dict = {}
    if "pools" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.pool_information_list

        out["Pools"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.pool_information_list.serialize_aws_json_1_0(
                value["pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribePoolsResult:
    out: DescribePoolsResult = {}  # type: ignore[typeddict-item]
    if "Pools" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.pool_information_list

        out["pools"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.pool_information_list.deserialize_aws_json_1_0(
                data["Pools"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
