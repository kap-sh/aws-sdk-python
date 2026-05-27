"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrunkInterfaceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_trunk_interface_associations_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trunk_interface_association_id_list


class DescribeTrunkInterfaceAssociationsRequest(TypedDict):
    association_ids: NotRequired[
        "aws_sdk_ec2.types.trunk_interface_association_id_list.TrunkInterfaceAssociationIdList"
    ]
    """<p>The IDs of the associations.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>gre-key</code> - The ID of a trunk interface association.</p> </li> <li> <p> <code>interface-protocol</code> - The interface protocol. Valid values are <code>VLAN</code> and <code>GRE</code>.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_trunk_interface_associations_max_results.DescribeTrunkInterfaceAssociationsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
