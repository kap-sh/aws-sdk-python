"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfacePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_network_interface_permissions_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.network_interface_permission_id_list
    import aws_sdk_ec2.types.string


class DescribeNetworkInterfacePermissionsRequest(TypedDict, closed=True):
    network_interface_permission_ids: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission_id_list.NetworkInterfacePermissionIdList"
    ]
    """<p>The network interface permission IDs.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>network-interface-permission.network-interface-permission-id</code> - The ID of the permission.</p> </li> <li> <p> <code>network-interface-permission.network-interface-id</code> - The ID of the network interface.</p> </li> <li> <p> <code>network-interface-permission.aws-account-id</code> - The Amazon Web Services account ID.</p> </li> <li> <p> <code>network-interface-permission.aws-service</code> - The Amazon Web Services service.</p> </li> <li> <p> <code>network-interface-permission.permission</code> - The type of permission (<code>INSTANCE-ATTACH</code> | <code>EIP-ASSOCIATE</code>).</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_network_interface_permissions_max_results.DescribeNetworkInterfacePermissionsMaxResults"
    ]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. If this parameter is not specified, up to 50 results are returned by default. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInterfacePermissionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_interface_permission_ids" in value:
        import aws_sdk_ec2.types.network_interface_permission_id_list

        aws_sdk_ec2.types.network_interface_permission_id_list.serialize_ec2_query(
            value["network_interface_permission_ids"],
            pairs,
            f"{prefix}.NetworkInterfacePermissionIds",
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInterfacePermissionsRequest:
    out: DescribeNetworkInterfacePermissionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInterfacePermissionIds") is not None:
        import aws_sdk_ec2.types.network_interface_permission_id_list

        out["network_interface_permission_ids"] = (
            aws_sdk_ec2.types.network_interface_permission_id_list.deserialize_ec2_query(
                el, "NetworkInterfacePermissionIds"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
