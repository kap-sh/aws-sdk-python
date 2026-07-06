"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDeviceFleetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.list_device_fleets_sort_by
    import aws_sdk_sagemaker.types.list_max_results
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListDeviceFleetsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.list_max_results.ListMaxResults"]
    """<p>The maximum number of results to select.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter fleets where packaging job was created after specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter fleets where the edge packaging job was created before specified time.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Select fleets where the job was updated after X</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>Select fleets where the job was updated before X</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>Filter for fleets containing this name in their fleet device name.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.list_device_fleets_sort_by.ListDeviceFleetsSortBy"
    ]
    """<p>The column to sort by.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>What direction to sort in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeviceFleetsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.list_device_fleets_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.list_device_fleets_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeviceFleetsRequest:
    out: ListDeviceFleetsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.list_device_fleets_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.list_device_fleets_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
