"""Generated from Smithy shape ``com.amazonaws.connect#ListChildHoursOfOperationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.child_hours_of_operations_list
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class ListChildHoursOfOperationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    child_hours_of_operations_summary_list: NotRequired[
        "aws_sdk_connect.types.child_hours_of_operations_list.ChildHoursOfOperationsList"
    ]
    """<p>Information about the hours of operation.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChildHoursOfOperationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "child_hours_of_operations_summary_list" in value:
        import aws_sdk_connect.types.child_hours_of_operations_list

        out["ChildHoursOfOperationsSummaryList"] = (
            aws_sdk_connect.types.child_hours_of_operations_list.serialize_json(
                value["child_hours_of_operations_summary_list"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListChildHoursOfOperationsResponse:
    out: ListChildHoursOfOperationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ChildHoursOfOperationsSummaryList" in data:
        import aws_sdk_connect.types.child_hours_of_operations_list

        out["child_hours_of_operations_summary_list"] = (
            aws_sdk_connect.types.child_hours_of_operations_list.deserialize_json(
                data["ChildHoursOfOperationsSummaryList"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
