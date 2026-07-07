"""Generated from Smithy shape ``com.amazonaws.route53domains#ListOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.list_operations_sort_attribute_name
    import aws_sdk_route_53_domains.types.operation_status_list
    import aws_sdk_route_53_domains.types.operation_type_list
    import aws_sdk_route_53_domains.types.page_marker
    import aws_sdk_route_53_domains.types.page_max_items
    import aws_sdk_route_53_domains.types.sort_order
    import aws_sdk_route_53_domains.types.timestamp


class ListOperationsRequest(TypedDict, closed=True):
    submitted_since: NotRequired["aws_sdk_route_53_domains.types.timestamp.Timestamp"]
    """<p>An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>"""
    marker: NotRequired["aws_sdk_route_53_domains.types.page_marker.PageMarker"]
    """<p>For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional operations. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element.</p>"""
    max_items: NotRequired["aws_sdk_route_53_domains.types.page_max_items.PageMaxItems"]
    """<p>Number of domains to be returned.</p> <p>Default: 20</p>"""
    status: NotRequired[
        "aws_sdk_route_53_domains.types.operation_status_list.OperationStatusList"
    ]
    """<p> The status of the operations. </p>"""
    type: NotRequired[
        "aws_sdk_route_53_domains.types.operation_type_list.OperationTypeList"
    ]
    """<p> An arrays of the domains operation types. </p>"""
    sort_by: NotRequired[
        "aws_sdk_route_53_domains.types.list_operations_sort_attribute_name.ListOperationsSortAttributeName"
    ]
    """<p> The sort type for returned values. </p>"""
    sort_order: NotRequired["aws_sdk_route_53_domains.types.sort_order.SortOrder"]
    """<p> The sort order for returned values, either ascending or descending. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOperationsRequest) -> dict:
    out: dict = {}
    if "submitted_since" in value:
        import aws_sdk_route_53_domains.types.timestamp

        out["SubmittedSince"] = (
            aws_sdk_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["submitted_since"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "status" in value:
        import aws_sdk_route_53_domains.types.operation_status_list

        out["Status"] = (
            aws_sdk_route_53_domains.types.operation_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "type" in value:
        import aws_sdk_route_53_domains.types.operation_type_list

        out["Type"] = (
            aws_sdk_route_53_domains.types.operation_type_list.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_route_53_domains.types.list_operations_sort_attribute_name

        out["SortBy"] = (
            aws_sdk_route_53_domains.types.list_operations_sort_attribute_name.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_route_53_domains.types.sort_order

        out["SortOrder"] = (
            aws_sdk_route_53_domains.types.sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOperationsRequest:
    out: ListOperationsRequest = {}  # type: ignore[typeddict-item]
    if "SubmittedSince" in data:
        import aws_sdk_route_53_domains.types.timestamp

        out["submitted_since"] = (
            aws_sdk_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedSince"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "Status" in data:
        import aws_sdk_route_53_domains.types.operation_status_list

        out["status"] = (
            aws_sdk_route_53_domains.types.operation_status_list.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Type" in data:
        import aws_sdk_route_53_domains.types.operation_type_list

        out["type"] = (
            aws_sdk_route_53_domains.types.operation_type_list.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_route_53_domains.types.list_operations_sort_attribute_name

        out["sort_by"] = (
            aws_sdk_route_53_domains.types.list_operations_sort_attribute_name.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_route_53_domains.types.sort_order

        out["sort_order"] = (
            aws_sdk_route_53_domains.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out
