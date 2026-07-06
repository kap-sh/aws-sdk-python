"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetInsightSelectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.string


class GetInsightSelectorsRequest(TypedDict, closed=True):
    trail_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If you specify a trail ARN, it must be in the format:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>You cannot use this parameter with the <code>EventDataStore</code> parameter.</p>"""
    event_data_store: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p> Specifies the ARN (or ID suffix of the ARN) of the event data store for which you want to get Insights selectors. </p> <p>You cannot use this parameter with the <code>TrailName</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInsightSelectorsRequest) -> dict:
    out: dict = {}
    if "trail_name" in value:
        out["TrailName"] = value["trail_name"]
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInsightSelectorsRequest:
    out: GetInsightSelectorsRequest = {}  # type: ignore[typeddict-item]
    if "TrailName" in data:
        out["trail_name"] = data["TrailName"]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    return out
