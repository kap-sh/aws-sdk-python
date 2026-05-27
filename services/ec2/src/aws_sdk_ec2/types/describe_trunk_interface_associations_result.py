"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrunkInterfaceAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trunk_interface_association_list


class DescribeTrunkInterfaceAssociationsResult(TypedDict):
    interface_associations: NotRequired[
        "aws_sdk_ec2.types.trunk_interface_association_list.TrunkInterfaceAssociationList"
    ]
    """<p>Information about the trunk associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
