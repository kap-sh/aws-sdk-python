"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeServiceUpdatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.service_update_list
    import aws_sdk_memorydb.types.string


class DescribeServiceUpdatesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    service_updates: NotRequired[
        "aws_sdk_memorydb.types.service_update_list.ServiceUpdateList"
    ]
    """<p>A list of service updates</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceUpdatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_updates" in value:
        import aws_sdk_memorydb.types.service_update_list

        out["ServiceUpdates"] = (
            aws_sdk_memorydb.types.service_update_list.serialize_aws_json_1_1(
                value["service_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceUpdatesResponse:
    out: DescribeServiceUpdatesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServiceUpdates" in data:
        import aws_sdk_memorydb.types.service_update_list

        out["service_updates"] = (
            aws_sdk_memorydb.types.service_update_list.deserialize_aws_json_1_1(
                data["ServiceUpdates"]
            )
        )
    return out
