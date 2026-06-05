"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityManagerDataExportsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_data_export_id_set
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_request_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityManagerDataExportsRequest(TypedDict):
    capacity_manager_data_export_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id_set.CapacityManagerDataExportIdSet"
    ]
    """<p> The IDs of the data export configurations to describe. If not specified, all export configurations are returned. </p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_manager_data_exports_request_max_results.DescribeCapacityManagerDataExportsRequestMaxResults"
    ]
    """<p> The maximum number of results to return in a single call. If not specified, up to 1000 results are returned. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token for the next page of results. Use this value in a subsequent call to retrieve additional results. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p> One or more filters to narrow the results. Supported filters include export status, creation date, and S3 bucket name. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityManagerDataExportsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_manager_data_export_ids" in value:
        import aws_sdk_ec2.types.capacity_manager_data_export_id_set

        aws_sdk_ec2.types.capacity_manager_data_export_id_set.serialize_ec2_query(
            value["capacity_manager_data_export_ids"],
            pairs,
            f"{prefix}.CapacityManagerDataExportIds",
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribeCapacityManagerDataExportsRequest:
    out: DescribeCapacityManagerDataExportsRequest = {}  # type: ignore[typeddict-item]
    if el.find("CapacityManagerDataExportIds") is not None:
        import aws_sdk_ec2.types.capacity_manager_data_export_id_set

        out["capacity_manager_data_export_ids"] = (
            aws_sdk_ec2.types.capacity_manager_data_export_id_set.deserialize_ec2_query(
                el, "CapacityManagerDataExportIds"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    return out
