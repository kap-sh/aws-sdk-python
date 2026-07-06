"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListResourceInventoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_integer
    import aws_sdk_license_manager.types.inventory_filter_list
    import aws_sdk_license_manager.types.string


class ListResourceInventoryRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    filters: NotRequired[
        "aws_sdk_license_manager.types.inventory_filter_list.InventoryFilterList"
    ]
    """<p>Filters to scope the results. The following filters and logical operators are supported:</p> <ul> <li> <p> <code>account_id</code> - The ID of the Amazon Web Services account that owns the resource. Logical operators are <code>EQUALS</code> | <code>NOT_EQUALS</code>.</p> </li> <li> <p> <code>application_name</code> - The name of the application. Logical operators are <code>EQUALS</code> | <code>BEGINS_WITH</code>.</p> </li> <li> <p> <code>license_included</code> - The type of license included. Logical operators are <code>EQUALS</code> | <code>NOT_EQUALS</code>. Possible values are <code>sql-server-enterprise</code> | <code>sql-server-standard</code> | <code>sql-server-web</code> | <code>windows-server-datacenter</code>.</p> </li> <li> <p> <code>platform</code> - The platform of the resource. Logical operators are <code>EQUALS</code> | <code>BEGINS_WITH</code>.</p> </li> <li> <p> <code>resource_id</code> - The ID of the resource. Logical operators are <code>EQUALS</code> | <code>NOT_EQUALS</code>.</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Logical operators are <code>EQUALS</code> (single account) or <code>EQUALS</code> | <code>NOT_EQUALS</code> (cross account).</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceInventoryRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_license_manager.types.inventory_filter_list

        out["Filters"] = (
            aws_sdk_license_manager.types.inventory_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceInventoryRequest:
    out: ListResourceInventoryRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_license_manager.types.inventory_filter_list

        out["filters"] = (
            aws_sdk_license_manager.types.inventory_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
