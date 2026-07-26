"""Generated from Smithy shape ``com.amazonaws.lightsail#GetCloudFormationStackRecordsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.cloud_formation_stack_record_list
    import capo_lightsail.types.string


class GetCloudFormationStackRecordsResult(TypedDict, closed=True):
    cloud_formation_stack_records: NotRequired[
        "capo_lightsail.types.cloud_formation_stack_record_list.CloudFormationStackRecordList"
    ]
    """<p>A list of objects describing the CloudFormation stack records.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetCloudFormationStackRecords</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCloudFormationStackRecordsResult) -> dict:
    out: dict = {}
    if "cloud_formation_stack_records" in value:
        import capo_lightsail.types.cloud_formation_stack_record_list

        out["cloudFormationStackRecords"] = (
            capo_lightsail.types.cloud_formation_stack_record_list.serialize_aws_json_1_1(
                value["cloud_formation_stack_records"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCloudFormationStackRecordsResult:
    out: GetCloudFormationStackRecordsResult = {}  # type: ignore[typeddict-item]
    if "cloudFormationStackRecords" in data:
        import capo_lightsail.types.cloud_formation_stack_record_list

        out["cloud_formation_stack_records"] = (
            capo_lightsail.types.cloud_formation_stack_record_list.deserialize_aws_json_1_1(
                data["cloudFormationStackRecords"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
